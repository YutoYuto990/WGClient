import requests
import os
import json
from dictionary import Dict
api=os.getenv("wows_api")
access_token=os.getenv("access_token")
class NoPlayerFound(Exception):
  pass
class Wows:
  def __init__(self,conv=dict):
    self.conv=conv
  def conv2url(self,about,**params):
    param="".join([f"&{i}={params[i]}" for i in params])
    if about.count("/")==1:
      return f"https://api.worldofwarships.asia/wows/{about}/?application_id={api}{param}"
  def get_json(self,about,**params) -> dict:
    data=json.loads(requests.get(self.conv2url(about,**params)).content)
    return data
  def _get_player_id(self,locale,name) -> dict:
    url=f"https://api.worldofwarships.{locale}/wows/account/list/?application_id={api}&search={name}"
    req=requests.get(url).content
    ret=json.loads(req)
    if ret["status"]=="ok":
      return ret["data"]
    else:
      raise NoPlayerFound("Player Not Found")
  def get_player(self,locale,name):
    
      pid=self._get_player_id(locale,name)[0]["account_id"]
      return self.conv(json.loads(requests.get(f"https://api.worldofwarships.{locale}/wows/account/info/?application_id={api}&account_id={pid}&extra=private.port&access_token={access_token}").content)["data"][str(pid)])
    #except:
     # return NoPlayerFound("player not found")
  def get_player_ships(self,locale,name):
    pid=self._get_player_id(locale,name)[0]["account_id"]
    return json.loads(requests.get(f"https://api.worldofwarships.asia/wows/ships/stats/?application_id={api}&account_id={pid}").content)["data"][str(pid)]
  def _get_ship_id(self,name):
    for i in range(1,100):
      ships=self.get_json("encyclopedia/ships",page_no=i,language="ja")
      try:
        for i in ships["data"]:
          if ships["data"][i]["name"]==name:
            return i
      except Exception as e:
        raise e
  def get_ship_data(self,name):
    try:
      sid=self._get_ship_id(name) if isinstance(name,str) else name
      details=self.get_json("encyclopedia/ships",ship_id=sid,language="ja")["data"][str(sid)]
      data=self.get_json("encyclopedia/shipprofile",ship_id=sid,language="ja")
      data["data"][str(sid)]["details"]=details
      return self.conv(data["data"][str(sid)])
    except Exception as e:
      raise e
  def get_arena(self,name=None):
    data=self.get_json("encyclopedia/battlearenas",language="ja")
    if not name:
      return self.conv(data)
    else:
      for i in data["data"]:
        if data["data"][i]["name"]==name:
          return self.conv(data["data"][i])