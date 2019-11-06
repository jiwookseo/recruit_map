import json
import requests
import os
from pprint import pprint as pp


class Maps:
    API_KEY = os.environ["GOOGLE_MAPS_KEY"]
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))

    @classmethod
    def directions(cls, origin, destination):
        path = cls.BASE_DIR + \
            "/directions/{}&{}.json".format(origin, destination)
        if os.path.isfile(path + "-w"):  # 도보가 더 빠른 경로 이력
            with open(path + "-w", encoding='UTF8') as f:
                res = json.load(f)
        elif os.path.isfile(path):  # 기존에 검색한 이력이 있을 때
            with open(path, encoding='UTF8') as f:
                res = json.load(f)
        else:
            URL = "https://maps.googleapis.com/maps/api/directions/json?origin=place_id:{}&destination=place_id:{}&mode=transit&language=ko&key={}".format(
                origin, destination, cls.API_KEY)
            res = requests.get(URL).json()
        # json data save
            if res["status"] == "OK":
                with open(path, 'w', encoding='UTF-8') as f:
                    json.dump(res, f, indent="  ", ensure_ascii=False)
                if res["routes"][0]["legs"][0]["duration"]["value"] < 1200:  # 20분 이하 거리는 도보와 시간 비교
                    transit = res["routes"][0]["legs"][0]["duration"]["value"]
                    URL = "https://maps.googleapis.com/maps/api/directions/json?origin=place_id:{}&destination=place_id:{}&mode=walking&language=ko&key={}".format(
                        origin, destination, cls.API_KEY)
                    res2 = requests.get(URL).json()
                    if res2["status"] == "OK":
                        walking = res2["routes"][0]["legs"][0]["duration"]["value"]
                        if walking < transit:
                            res = res2
                            with open(path + "-w", 'w', encoding='UTF-8') as f:
                                json.dump(res, f, indent="  ",
                                          ensure_ascii=False)
                    else:
                        res2["status"]
            else:
                print(URL)
                print(res["status"])
                return False
        return res["routes"][0]["legs"][0]["duration"]["value"] // 60

    @classmethod
    def places(cls, place):
        path = cls.BASE_DIR + "/places/{}.json".format(place)
        if os.path.isfile(path):  # 기존에 검색한 이력이 있을 때
            with open(path, encoding='UTF8') as f:
                res = json.load(f)
        else:
            URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={}&inputtype=textquery&fields=formatted_address,name,geometry,place_id&key={}".format(
                place, cls.API_KEY)
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
