from ..util.utils import get_json
from .exception import *


class Clan:

    def __init__(self, application_id, conv, lang, name=None):
        self.application_id = application_id
        self.conv = conv
        self.lang = lang
        self.value = self.conv(self._get_clan_data(name))
        self.origin = self._get_clan_data(name)

    def _get_clan_id(self, name=None):
        for i in range(1, 100):
            clans = get_json(self.application_id,
                             "clan/list",
                             page_no=i,
                             language=self.lang)
            for cl in clans["data"]:
                if  cl["name"]== name:
                    self.clan_id=cl["clan_id"]
                    return cl
        raise ClanNotFound("clan not found")

    def _get_clan_data(self, name):
        data = get_json(self.application_id,
                        "clan/info",
                        language=self.lang,
                        clan_id=self.clan_id)
        return data["data"]

    def __str__(self):
        return str(self.origin)
