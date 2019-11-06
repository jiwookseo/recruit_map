from pprint import pprint as pp
import requests
import os
from data_parser import Parser
from route import Route
from progress import progress_bar
from datetime import datetime
import json

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def load_data(key, page):
    path = BASE_DIR + "/saramin/{}-{}.json".format(
        datetime.now().strftime("%y%m%d%H"), page)
    if os.path.isfile(path):
        with open(path, encoding='UTF8') as f:
            res = json.load(f)
        return res, len(res["jobs"]["job"])
    else:
        URL = "http://oapi.saramin.co.kr/job-search/?access-key={}&start={}&sr=directhire&loc_cd=101000, 102000&ind_cd=3&bbs_gb=1&count=100&job_type=1,11&fields=keyword-code".format(
            key, page)
        res = requests.get(URL).json()
        try:
            length = len(res["jobs"]["job"])
            with open(path, 'w', encoding='UTF-8') as f:
                json.dump(res, f, indent="  ", ensure_ascii=False)
            return res, length
        except KeyError:
            print(res["message"])
            return {}, 0


print("==============   Jobs Start    ==============")
api_key = os.environ.get("SARAMIN_KEY")
count = 0
page = 0
res, length = load_data(api_key, page)
total = int(res["jobs"]["total"])
print("total : {} jobs exist".format(total))
while length:
    for i in range(length):
        # progress bar
        progress_bar(i + count, total, 20)
        # parser data initialization
        parser = Parser(res["jobs"]["job"][i])
        # scrap company and job
        parser.scrap_company()
        parser.scrap_job()
    page += 1
    count += length
    if length == 100:
        res, length = load_data(api_key, page)
        total = int(res["jobs"]["total"])
    else:
        break

print("\n==============   Jobs Finish   ==============")
print("==============  Routes Start   ==============")
Route.create_routes()
print("\n==============  Routes Finish  ==============")
