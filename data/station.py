from google_maps import Maps
import json
import os
import requests
from pprint import pprint as pp

NODE_ENV = os.environ.get("NODE_ENV", "develop")
API_URL = "http://recruitmap.ninja:8000/api/" if NODE_ENV == "production" else "http://127.0.0.1:8000/api/"

with open("stations/data.json", encoding="UTF8") as f:
    raw = json.load(f)["DATA"]
data = []
stations = {}
for obj in raw:
    name, address, line = obj["station_nm"], obj["address"], obj["line_num"]
    if name and address and line:
        if name not in stations:
            stations[name] = {"address": address, "line": {line}}
        else:
            stations[name]["line"].add(line)
# print(len(stations))
for name, v in stations.items():
    station = stations[name]
    station["name"] = name
    # reference : db settings document / line code table
    station["line"] = ",".join(sorted(v["line"]))
    place = Maps.places(station["address"])
    if not place:
        place = Maps.places(name + "역")
    if place:
        station["place_id"] = place["place_id"]
        station["address"] += " {}역".format(name)
        station["lat"] = place["geometry"]["location"]["lat"]
        station["lng"] = place["geometry"]["location"]["lng"]
    else:
        print(name, station["address"])

    # create request
    req = requests.post(API_URL + "stations/", station)
    res = req.json()
    if req.status_code != 201:
        pp(res)
        pp(station)

# with open("stations/objects.json", 'w', encoding="UTF-8") as f:
#     json.dump(stations, f, indent="  ", ensure_ascii=False)
