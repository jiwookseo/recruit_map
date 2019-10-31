import requests
import os
import json
from google_maps import Maps
from progress import progress_bar
from pprint import pprint as pp


class Route:
    NODE_ENV = os.environ.get("NODE_ENV", "develop")
    API_URL = "http://52.78.29.170:8000/api/" if NODE_ENV == "production" else "http://127.0.0.1:8000/api/"
    API = requests.get(API_URL).json()

    @classmethod
    def create_routes(cls):
        res = requests.get(cls.API["companies"]+"?all")
        companies = res.json()

        res = requests.get(cls.API["stations"]+"?all")
        stations = res.json()

        print("=== {} companies and {} stations exist  ==="
              .format(len(companies), len(stations)))
        print("=============================================")
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json'}
        for j in range(len(stations)):  # len(stations) 까지 하면 월 사용량 이상으로 사용됨
            # progress bar
            progress_bar(j, len(stations), 20)
            station = stations[j]
            data = []
            res = requests.get(station["routes"])
            count = len(res.json()["results"])

            # already finished
            if count >= len(companies):
                continue
            # not finished
            for i in (61,):
                company = companies[i]
                time = Maps.directions(
                    stations[j]["place_id"], companies[i]["place_id"])
                if time:
                    route = {"company": company["id"],
                             "station": station["id"], "time": time}
                    data.append(route)
            requests.post(cls.API["routes"],
                          json=json.dumps(data), headers=headers)
