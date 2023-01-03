import requests
import os
import json
from .utility.convdict import Dict
from .player import Player
from .ship import Ship
from .arena import Arena
from .commander import Commander
from .exception import *


class App:
  def __init__(self,application_id,lang="ja",convert=False):
    self.conv=Dict if convert else dict
    self.lang=lang
    if application_id:
      self.application_id=application_id
    else:
      raise InvalidApplicationId("Invalid application id provided.")

  def get_player(self,name,locale=None):
    player=Player(self.application_id,self.conv,name,locale)
    return player

  def get_ship(self,name_or_id):
    ship=Ship(self.application_id,self.conv,self.lang,name_or_id)
    return ship

  def get_arena(self,name=None):
    arena=Arena(self.application_id,self.conv,self.lang,name)
    return arena

  def get_commander(self,name_or_id=None):
    commander=Commander(self.application_id,self.conv,self.lang,name_or_id)
    return commander