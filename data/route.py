import requests
import os
import json
from google_maps import Maps
from progress import progress_bar
from pprint import pprint as pp


class Route:
    NODE_ENV = os.environ.get("NODE_ENV", "develop")
    API_URL = "http://www.recruitmap.ninja:8000/api/" if NODE_ENV == "production" else "http://127.0.0.1:8000/api/"
    API = requests.get(API_URL).json()

    @classmethod
    def get_route(cls, pk):
        req = requests.get("{}{}/".format(cls.API["routes"], pk))
        res = req.json()
        return True if req.status_code == 200 else False, res

    @classmethod
    def create_route(cls, data, headers=None):
        if headers:
            req = requests.post(cls.API["routes"],
                                json=json.dumps(data), headers=headers)
        else:
            req = requests.post(cls.API["routes"], data)
        try:
            res = req.json()
            return True if req.status_code == 201 else False, res
        except json.decoder.JSONDecodeError:
            for item in data:
                req = requests.post(cls.API["routes"], item)
            return True

    @classmethod
    def update_route(cls, pk, data):
        req = requests.put("{}{}/".format(cls.API
                                          ["routes"], pk), data)
        res = req.json()
        return True if req.status_code == 200 else False, res

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
            routes = res.json()["results"]
            count = len(routes)
            # already finished
            if count >= len(companies):
                continue
            # not finished
            for i in range(count, len(companies)):
                company = companies[i]
                time = Maps.directions(
                    station["place_id"], companies[i]["place_id"])
                if time:
                    route = {"company": company["id"],
                             "station": station["id"], "time": time}
                    data.append(route)
            cls.create_route(data, headers)
            res = requests.get(station["routes"])
            routes = res.json()["results"]
            count = len(routes)
            # already finished
            if count >= len(companies):
                continue
            # not finished
            for i in range(len(companies)):
                company = companies[i]
                time = Maps.directions(
                    station["place_id"], companies[i]["place_id"])
                if time:
                    route = {"company": company["id"],
                             "station": station["id"], "time": time}
                    data.append(route)
            cls.create_route(data, headers)
