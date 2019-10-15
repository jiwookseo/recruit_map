import json
import requests
import os


class Maps:
    def __init__(self, key):
        self.api_key = key

    def directions(self, origin, destination):
        URL = "https://maps.googleapis.com/maps/api/directions/json?origin=place_id:{}&destination=place_id:{}&mode=transit&arrival_time=1571097600&key={}".format(
            origin, destination, self.api_key)
        res = requests.get(URL).json()
        # json data save
        with open("directions/{}&{}.json".format(
                origin, destination), 'w', encoding='utf-8') as f:
            json.dump(res, f, indent="\t")
        if res["status"] == "OK":
            return res["routes"][0]["legs"][0]["duration"]["text"]
        else:
            print(res["status"])

    def places(self, place):
        URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={}&inputtype=textquery&fields=formatted_address,name,geometry,place_id&key={}".format(
            place, self.api_key)
        res = requests.get(URL).json()
        # json data save
        with open("places/{}.json".format(res["candidates"][0]["place_id"]), 'w', encoding='utf-8') as f:
            json.dump(res, f, indent="\t")
        if res["status"] == "OK":
            return res["candidates"][0]
            # output shape = {name, formatted_address, geomtry: {viewport: {southwest, northeast}, location, place_id}}
        else:
            print(res["status"])


key = os.environ.get("GOOGLE_MAPS_KEY")
maps = Maps(key)
station = maps.places("명일역")  # Station data
# TODO station data save
company = maps.places("네이버 본사")  # Company data
# TODO company data save
print(maps.directions(station["place_id"], company["place_id"]))
