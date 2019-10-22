from googleMaps import Maps
import json
from pprint import pprint as pp

with open("stations/data.json", encoding='UTF8') as f:
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
    # reference : db settings document / line code table
    station["line"] = ",".join(sorted(v["line"]))
    place = Maps.places(station["address"])
    if not place:
        place = Maps.places(name + "역")
    if place:
        station["place_id"] = place["place_id"]
        station["address"] = "{} {}역".format(place["formatted_address"], name)
        station["viewport"] = place["geometry"]["viewport"]
        station["lat"] = place["geometry"]["location"]["lat"]
        station["lng"] = place["geometry"]["location"]["lng"]
    else:
        print(name, station["address"])
pp(stations)
