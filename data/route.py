import requests
import os
import json
from googleMaps import Maps
from pprint import pprint as pp

NODE_ENV = os.environ.get("NODE_ENV", "develop")
API_URL = "http://52.78.29.170:8000/api/" if NODE_ENV == "production" else "http://127.0.0.1:8000/api/"

res = requests.get(API_URL + "companies/")
count = res.json()["count"]
res = requests.get(API_URL + "companies/?limit={}".format(count))
companies = res.json()["results"]

res = requests.get(API_URL + "stations/")
count = res.json()["count"]
res = requests.get(API_URL + "stations/?limit={}".format(count))
stations = res.json()["results"]

print("{} stations * {} companies = {} routes"
      .format(len(companies), len(stations), len(companies) * len(stations)))

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
for j in range(200, 260):  # len(stations) 까지 하면 월 사용량 이상으로 사용됨
    station = stations[j]
    data = []
    print("station no.{} {}".format(j, station["name"]))
    res = requests.get(API_URL + "routes/?station={}".format(station["id"]))
    count = res.json()["count"]
    if count >= len(companies):
        continue
    for i in range(len(companies)):
        company = companies[i]
        time = Maps.directions(
            stations[j]["place_id"], companies[i]["place_id"])
        if time:
            route = {"company": company["id"],
                     "station": station["id"], "time": time}
            data.append(route)
        if count:
            req = requests.post(API_URL + "routes/",
                                json=route, headers=headers)
    if not count:
        req = requests.post(API_URL + "routes/",
                            json=json.dumps(data), headers=headers)
