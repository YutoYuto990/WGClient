import requests
import json
from .exception import *
from .ship import Ship
import matplotlib.pyplot as plt


class Player:

    def __init__(self, application_id, conv, lang, name, locale=None):
        locations = ["eu", "ne", "asia"]
        self.lang = lang
        self.conv = conv
        self.application_id = application_id
        self.name = name
        res = None
        if locale:
            res = self._get_player_id(name, locale)
            self.account_id = res["account_id"]
            self.locale = locale
            self.name = res["nickname"]
        else:
            for i in locations:
                try:
                    res = self._get_player_id(name, i)
                except:
                    continue
                if res:
                    break
            if res:
                self.locale = i
                self.name = res["nickname"]
                self.account_id = res["account_id"]
            else:
                raise PlayerNotFound("Player Not Found")
        self.value = self.conv(self._get_player())
        self.origin = self._get_player()

    def _get_player_id(self, name, locale) -> dict:
        url = f"https://api.worldofwarships.{locale}/wows/account/list/?application_id={self.application_id}&search={name}"
        resp = requests.get(url)
        req = resp.content
        ret = json.loads(req)
        if ret["status"] == "ok":
            return ret["data"][0]
        else:
            raise PlayerNotFound("Player Not Found")

    def _get_player(self):
        pid = self._get_player_id(self.name, self.locale)["account_id"]
        return json.loads(
            requests.get(
                f"https://api.worldofwarships.{self.locale}/wows/account/info/?application_id={self.application_id}&account_id={pid}"
            ).content)["data"][str(pid)]

    def using_ships(self):
        resp = json.loads(
            requests.get(
                f"https://api.worldofwarships.{self.locale}/wows/ships/stats/?application_id={self.application_id}&account_id={self.account_id}"
            ).content)["data"][str(self.account_id)]
        return resp

    def achievements(self):
        url=f"https://api.worldofwarships.{self.locale}/wows/account/achievements/?application_id={self.application_id}&account_id={self.account_id}"
        resp=json.loads(requests.get(url).content)["data"][str(self.account_id)]
        return resp

    def __str__(self):
        return str(self.origin)
