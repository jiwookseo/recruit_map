import json
import requests
import os


class Maps:
    api_key = os.environ.get("GOOGLE_MAPS_KEY")

    @classmethod
    def directions(cls, origin, destination):
        path = "directions/{}&{}.json".format(origin, destination)
        if os.path.isfile(path):  # 기존에 검색한 이력이 있을 때
            with open(path, encoding='UTF8') as f:
                res = json.load(f)
        else:
            URL = "https://maps.googleapis.com/maps/api/directions/json?origin=place_id:{}&destination=place_id:{}&mode=transit&arrival_time=1571097600&language=ko&key={}".format(
                origin, destination, cls.api_key)
            print(URL)
            res = requests.get(URL).json()
        # json data save
            if res["status"] == "OK":
                with open(path, 'w', encoding='UTF-8') as f:
                    json.dump(res, f, indent="\t", ensure_ascii=False)
            else:
                print(res["status"])
                return False
        return res["routes"][0]["legs"][0]["duration"]["text"]

    @classmethod
    def places(cls, place):
        path = "places/{}.json".format(place)
        if os.path.isfile(path):  # 기존에 검색한 이력이 있을 때
            with open(path, encoding='UTF8') as f:
                res = json.load(f)
        else:
            URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={}&inputtype=textquery&fields=formatted_address,name,geometry,place_id&key={}".format(
                place, cls.api_key)
            res = requests.get(URL).json()
        # json data save
        if res["status"] == "OK":
            with open(path, 'w', encoding='UTF-8') as f:
                json.dump(res, f, indent="\t", ensure_ascii=False)
            return res["candidates"][0]
            # output shape = {name, formatted_address,location, place_id, geometry: {viewport: {southwest, northeast}}}
        else:
            print(res["status"])
            return False


# station = Maps.places("명일역")  # Station data
# company = Maps.places("경기 성남시 분당구 불정로 6")  # Company data
# print(Maps.directions(station["place_id"], company["place_id"]))
