import requests
import os
import json
from google_maps import Maps
from pprint import pprint as pp


class Route:
    NODE_ENV = os.environ.get("NODE_ENV", "develop")
    API_URL = "http://52.78.29.170:8000/api/" if NODE_ENV == "production" else "http://127.0.0.1:8000/api/"

    @classmethod
    def create_routes(cls):
        res = requests.get(cls.API_URL + "companies/?all")
        companies = res.json()

        res = requests.get(cls.API_URL + "stations/?all")
        stations = res.json()

        print("{} stations * {} companies = {} routes"
              .format(len(companies), len(stations), len(companies) * len(stations)))

        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json'}
        for j in range(len(stations)):  # len(stations) 까지 하면 월 사용량 이상으로 사용됨
            station = stations[j]
            data = []
            print("\rstation no.{} / {}".format(
                j, len(stations)), end=" "*5)
            res = requests.get(
                cls.API_URL + "routes/?station={}".format(station["id"]))
            count = res.json()["count"]

            # already finished
            if count >= len(companies):
                continue
            # not finished
            for i in range(count, len(companies)):
                company = companies[i]
                time = Maps.directions(
                    stations[j]["place_id"], companies[i]["place_id"])
                if time:
                    route = {"company": company["id"],
                             "station": station["id"], "time": time}
                    data.append(route)
            requests.post(cls.API_URL + "routes/",
                          json=json.dumps(data), headers=headers)
