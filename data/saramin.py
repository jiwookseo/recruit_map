from pprint import pprint as pp
import requests
import os
from data_parser import Parser
from route import Route

apiKey = os.environ.get("SARAMIN_KEY")
URL = "http://oapi.saramin.co.kr/job-search/?access-key={}&sr=directhire&loc_cd=101000, 102000&ind_cd=3&bbs_gb=1&count=100&job_type=1,11&fields=keyword-code".format(
    apiKey)
print("=============  공고 검색 시작  =============")
res = requests.get(URL).json()
total = int(res["jobs"]["total"])
count = 0
print("{}개 공고가 있습니다.".format(total))
while count < total:
    res = requests.get(URL+"&start={}".format(count)).json()
    length = len(res["jobs"]["job"])
    for i in range(length):
        print("\rjob no.{} / {}".format(i + 1 + count, total), end=" "*5)
        parser = Parser(res["jobs"]["job"][i])
        parser.scrap_company()
        parser.scrap_job()
    count += length

print("\n=============  공고 검색 종료  =============")
print("=============  경로 검색 시작  =============")
Route.create_routes()
print("\n=============  경로 검색 종료  =============")
