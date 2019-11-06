import requests
import os
import json
from bs4 import BeautifulSoup
from google_maps import Maps
from pprint import pprint as pp
from datetime import datetime


class Parser:
    NODE_ENV = os.environ.get("NODE_ENV", "develop")
    API_URL = "http://recruitmap.ninja:8000/api/" if NODE_ENV == "production" else "http://127.0.0.1:8000/api/"
    API = requests.get(API_URL).json()

    def __init__(self, data):
        self.data = data
        self.company = {}

    def scrap_company(self):
        name = self.data["company"]["detail"]["name"]
        exist, company = self.get_company(name)
        if exist:
            if company["scale"] and company["avg_salary"] and company["start_salary"]:
                return False, "Already exists"
            COMPANY_URL = company["url"]
        # init company dictionary
        company = {}

        # company data part
        company["name"] = name
        if self.data["company"]["detail"].get("href"):
            company["saramin_url"] = self.data["company"]["detail"]["href"]
        company["ind_code"] = self.data["position"]["industry"]["code"].replace(
            "|", ",")
        company["ind_name"] = self.data["position"]["industry"]["name"]
        company["ind_key_code"] = self.data["position"]["industry-keyword-code"].replace(
            "|", ",")
        company["ind_key_code"] = ",".join(
            company["ind_key_code"].split(",")[:5])

        # company scrap part
        saramin_url = company.get("saramin_url", False)
        company["avg_salary"] = company["start_salary"] = 0
        if saramin_url:
            res = requests.get(saramin_url)
            res = requests.get(res.url.replace(
                "view", "view-inner-salary"))
            soup = BeautifulSoup(res.text, "html.parser")
            salary_tag = soup.find("p", "average_currency")
            if salary_tag:
                salary_str = salary_tag.text.replace(
                    ",", "").replace("만원", "")
                company["avg_salary"] = int(salary_str.strip())
            start_tag = soup.find("p", "salary")
            if start_tag:
                salary_str = start_tag.text.replace(
                    ",", "").replace("만원", "")
                company["start_salary"] = int(salary_str.strip())
        res = requests.get(
            "http://www.jobkorea.co.kr/Search/?stext={}&tabType=corp&Page_No=1".format(company["name"]))
        soup = BeautifulSoup(res.text, "html.parser")
        corp = soup.find("div", "post-list-corp clear")
        if corp:
            link = corp.find("a")
            if link:
                res = requests.get(
                    "http://www.jobkorea.co.kr" + link["href"])
                soup = BeautifulSoup(res.text, "html.parser")
                keys = soup.find_all("div", "field-label")
                keys = [key.text for key in keys]
                containers = soup.find_all("div", "value-container")
                scrap = {}
                for key, container in zip(keys, containers):
                    if key == "대졸초임":
                        salary_tag = container.find(
                            "div", "salary-average-item")
                        if salary_tag:
                            salary = int(salary_tag.text.replace(
                                ",", "").replace("만원", ""))
                            company["start_salary"] += salary
                            company["start_salary"] //= 2
                    elif key != "계열사":
                        value = container.find("div", "value")
                        scrap[key] = value.text
                company["scale"] = scrap.get("기업구분", "")
                company["address"] = scrap.get("주소 ", "")
                company["href"] = scrap.get("홈페이지", "")
                if company["href"] == "-":
                    company["href"] = ""
                res = requests.get(res.url[:-4] + "Salary")
                soup = BeautifulSoup(res.text, "html.parser")
                salary_tag = soup.find("div", "salary")
                if salary_tag:
                    salary_str = salary_tag.find("div", "value").text
                    salary = int(salary_str.replace(",", ""))
                    company["avg_salary"] += salary
                    company["avg_salary"] //= 2
        # map part
        place = Maps.places(company["name"])
        if not place and company.get("address"):
            place = Maps.places(company["address"])
            if not place:
                place = Maps.places(company["address"].split("(")[0])
        if place:
            company["lat"] = place["geometry"]["location"]["lat"]
            company["lng"] = place["geometry"]["location"]["lng"]
            company["place_id"] = place["place_id"]
            if not company.get("address", False):
                company["address"] = place["formatted_address"]
        else:
            return False, "No place result"
        # create request
        if exist:
            req = requests.put(COMPANY_URL, company)
            res = req.json()
            if req.status_code == 200:
                company = res
                self.company = company
            else:
                print(company)
                print(res)
        else:
            created, res = self.create_company(company)
            if not created:
                print("\nCompany is not created")
                print(company)
                print(res)
                return False, res
            company = res
            self.company = company

        # json data save
        with open("companies/{}.json".format(name), 'w', encoding="UTF-8") as f:
            json.dump(company, f, indent="  ", ensure_ascii=False)
        return True, company

    def scrap_job(self):
        if not self.company:
            return False, "Not founded company"
        title = self.data["position"]["title"]
        open_stamp = datetime.fromtimestamp(
            float(self.data["opening-timestamp"])).strftime("%Y-%m-%dT%H:%M")
        exist, job = self.get_job(title, open_stamp)
        if exist:
            return False, "already exists"
        else:
            # init job dictionary
            job = {}
            job["saramin_url"] = self.data["url"]
            job["title"] = self.data["position"]["title"]
            category = self.data["position"]["job-category"]["name"]
            category = ",".join(category.split(",")[:5])
            job["job"] = category
            job["exp_min"] = self.data["position"]["experience-level"]["min"]
            job["exp_max"] = self.data["position"]["experience-level"]["max"]
            job["edu_code"] = self.data["position"]["required-education-level"]["code"]
            job["edu_name"] = self.data["position"]["required-education-level"]["name"]
            job["open"] = open_stamp
            job["close"] = datetime.fromtimestamp(
                float(self.data["expiration-timestamp"])).strftime("%Y-%m-%dT%H:%M")
            job["close_type"] = self.data["close-type"]["code"]
            job["company"] = self.company["id"]

            # create request
            created, res = self.create_job(job)
            if not created:
                print("\nJob is not created")
                print(job)
                print(res)
                return False, res
            job = res

            # json data save
            with open("jobs/{}_{}.json".format(title.replace("/", "+"), open_stamp), 'w', encoding="UTF-8") as f:
                json.dump(job, f, indent="  ", ensure_ascii=False)
            return True, job

    @classmethod
    def get_company(cls, name):
        res = requests.get(cls.API["companies"] + "?name=" + name).json()
        if res["count"]:
            return True, res["results"][0]
        else:
            return False, res

    @classmethod
    def create_company(cls, company):
        req = requests.post(cls.API["companies"], company)
        res = req.json()
        return True if req.status_code == 201 else False, res

    @classmethod
    def get_job(cls, title, open_stamp):
        res = requests.get(
            cls.API["jobs"] + "?title={}&open={}".format(title, open_stamp)).json()
        if res["count"]:
            return True, res["results"][0]
        else:
            return False, res

    @classmethod
    def create_job(cls, job):
        req = requests.post(cls.API["jobs"], job)
        res = req.json()
        return True if req.status_code == 201 else False, res
