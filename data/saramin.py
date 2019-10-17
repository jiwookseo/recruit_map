import requests
import os
from bs4 import BeautifulSoup
from googleMaps import Maps
from pprint import pprint as pp

apiKey = os.environ.get("SARAMIN_KEY")
URL = "http://oapi.saramin.co.kr/job-search/?access-key={}&sr=directhire&loc_cd=101000, 102000&ind_cd=3&bbs_gb=1&job_type=1,11&count=110&fields=keyword-code".format(
    apiKey)
res = requests.get(URL).json()
print(res["jobs"]["total"] + "개 공고가 있습니다.")
for job in res["jobs"]["job"]:
    result = {}
    # company part
    result["name"] = job["company"]["detail"]["name"]
    if job["company"]["detail"].get("href"):
        result["saramin_url"] = job["company"]["detail"]["href"]
    else:
        print(result["name"], "saramin_url 없는 기업")
    result["ind_code"] = job["position"]["industry"]["code"]
    result["ind_name"] = job["position"]["industry"]["name"]
    result["ind_key_code"] = job["position"]["industry-keyword-code"]
    #  map part
    res = requests.get(
        "http://www.jobkorea.co.kr/Search/?stext={}&tabType=corp&Page_No=1".format(result["name"]))
    soup = BeautifulSoup(res.text, "html.parser")
    company = soup.find("div", "post-list-corp clear").find("a")
    if company:
        if company.text != result["name"]:
            print(company.text, result["name"])
        res = requests.get("http://www.jobkorea.co.kr" + company["href"])
        soup = BeautifulSoup(res.text, "html.parser")
        keys = soup.find_all("div", "field-label")
        items = soup.find_all("div", "value")
        scrap = {key.text: item.text for key,
                 item in zip(keys[:-1], items[7:])}
        print(scrap)
        url = res.url[:4] + "Salary"
        # TODO 연봉 정보 받아올 수 있는 페이지
    break
    place = Maps.places(result["name"])
    if not place:
        place = Maps.places(scrap["주소 "])
    if place:
        result["address"] = place["formatted_address"]
        result["lat"] = place["geometry"]["location"]["lat"]
        result["lng"] = place["geometry"]["location"]["lng"]
        result["vp_ne_lat"] = place["geometry"]["viewport"]["northeast"]["lat"]
        result["vp_ne_lng"] = place["geometry"]["viewport"]["northeast"]["lng"]
        result["vp_sw_lat"] = place["geometry"]["viewport"]["southwest"]["lat"]
        result["vp_sw_lng"] = place["geometry"]["viewport"]["southwest"]["lng"]
        result["place_id"] = place["place_id"]
    else:
        print(result["name"])
    # job part
    result["job"] = job["position"]["job-category"]["name"]
    result["exp_min"] = job["position"]["experience-level"]["min"]
    result["exp_max"] = job["position"]["experience-level"]["max"]
    result["edu_code"] = job["position"]["required-education-level"]["code"]
    result["edu_name"] = job["position"]["required-education-level"]["name"]
    result["open"] = job["opening-timestamp"]
    result["close"] = job["expiration-timestamp"]
    result["close_type"] = job["close-type"]
