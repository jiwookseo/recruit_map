import json
import requests
import os


class Maps:
    api_key = "AIzaSyBqydbDQL01C34zWA3hVXEUVi2UQuMmbzQ"

    @classmethod
    def directions(cls, origin, destination):
        path = "directions/{}&{}.json".format(origin, destination)
        if os.path.isfile(path):  # 기존에 검색한 이력이 있을 때
            with open(path, encoding='UTF8') as f:
                res = json.load(f)
        else:
            URL = "https://maps.googleapis.com/maps/api/directions/json?origin=place_id:{}&destination=place_id:{}&mode=transit&language=ko&key={}".format(
                origin, destination, cls.api_key)
            res = requests.get(URL).json()
        # json data save
            if res["status"] == "OK":
                with open(path, 'w', encoding='UTF-8') as f:
                    json.dump(res, f, indent="  ", ensure_ascii=False)
            else:
                print(URL)
                print(res["status"])
                return False
        return res["routes"][0]["legs"][0]["duration"]["value"] // 60

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
                json.dump(res, f, indent="  ", ensure_ascii=False)
            return res["candidates"][0]
            # output shape = {name, formatted_address,location, place_id, geometry: {viewport: {southwest, northeast}}}
        else:
            # print(res["status"])
            return False


# station = Maps.places("명성교회")  # Station data
# company = Maps.places("명일엘지아파트")  # Company data
# print(Maps.directions(station["place_id"], company["place_id"]))
