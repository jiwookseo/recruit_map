import requests
import os

apiKey = os.environ.get("SARAMIN_KEY")
URL = "http://oapi.saramin.co.kr/job-search/?access-key={}&sr=directhire&loc_cd=101000, 102000&ind_cd=3&bbs_gb=1&count=110".format(
    apiKey)
res = requests.get(URL).json()
print(res["jobs"]["total"] + "개 공고가 있습니다.")

# .then(res= > {
#     console.log(res.data)
#     const jobs=res.data.jobs.job
#     jobs.forEach(job=> {
#         console.log(job.company.detail.name, "/", job.position.title)
#     })
# })
# // 기업 주소, 평균 연봉 등 데이터 수집 필요
