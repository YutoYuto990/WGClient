import requests
import os
import json
from ..util.convdict import Dict
from .player import Player
from .ship import Ship
from .arena import Arena
from .commander import Commander
from .clan import Clan
from .exception import *


class WowsApp:

    def __init__(self, application_id, lang="ja", convert=False):
        self.conv = Dict if convert else dict
        self.lang = lang
        self.application_id = application_id

    def get_player(self, name, locale=None) -> Player:
        player = Player(self.application_id, self.conv, self.lang, name,
                        locale)
        return player

    def get_ship(self, name_or_id) -> Ship:
        ship = Ship(self.application_id, self.conv, self.lang, name_or_id)
        return ship

    def get_arena(self, name=None) -> Arena:
        arena = Arena(self.application_id, self.conv, self.lang, name)
        return arena

    def get_commander(self, name_or_id=None) -> Commander:
        commander = Commander(self.application_id, self.conv, self.lang,
                              name_or_id)
        return commander

    def get_clan(self,name_or_id=None) -> Clan:
        clan=Clan(self.application_id, self.conv, self.lang,name_or_id)
        return clan
