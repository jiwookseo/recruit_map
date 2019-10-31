from pprint import pprint as pp
import requests
import os
from data_parser import Parser
from route import Route
from progress import progress_bar
import time

apiKey = os.environ.get("SARAMIN_KEY")
URL = "http://oapi.saramin.co.kr/job-search/?access-key={}&sr=directhire&loc_cd=101000, 102000&ind_cd=3&bbs_gb=1&count=100&job_type=1,11&fields=keyword-code".format(
    apiKey)
print("================   Jobs Start    ================")
res = requests.get(URL).json()
total = int(res["jobs"]["total"])
count = 0
print("total : {} jobs exist".format(total))
while count < total:
    res = requests.get(URL+"&start={}".format(count)).json()
    length = len(res["jobs"]["job"])
    for i in range(length):
        # progress bar
        progress_bar(i + 1 + count, total, 25, "▦")
        # parser data initialization
        parser = Parser(res["jobs"]["job"][i])
        # scrap company and job
        parser.scrap_company()
        parser.scrap_job()
    count += length

print("\n================   Jobs Finish   ================")
print("================  Routes Start   ================")
Route.create_routes()
print("================  Routes Finish  ================")
