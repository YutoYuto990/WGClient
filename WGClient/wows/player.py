import requests
import json
from .exception import *
from .ship import Ship
import matplotlib.pyplot as plt

class Player:
  def __init__(self,
               application_id,
               conv,
               name,
               locale=None):
    locations=["eu","ne","asia"]
    self.conv=conv
    self.usingships=None
    self.draw=None
    self.application_id=application_id
    self.name=name
    res=None
    if locale:
      res=self._get_player_id(name,locale)
      self.account_id=res["account_id"]
      self.locale=locale
      self.name=res["nickname"]
    else:
      for i in locations:
        try:
          res=self._get_player_id(name,i)
        except:
          continue
        if res:
          break
      if res:
        self.locale=i
        self.name=res["nickname"]
        self.account_id=res["account_id"]
      else:
        raise PlayerNotFound("Player Not Found")
    self.value=self.conv(self._get_player())
    self.origin=self._get_player()
  
  def _get_player_id(self,name,locale) -> dict:
    url=f"https://api.worldofwarships.{locale}/wows/account/list/?application_id={self.application_id}&search={name}"
    resp=requests.get(url)
    req=resp.content
    ret=json.loads(req)
    if ret["status"]=="ok":
      return ret["data"][0]
    else:
      raise PlayerNotFound("Player Not Found")

  def _get_player(self):
    
      pid=self._get_player_id(self.name,self.locale)["account_id"]
      return json.loads(requests.get(f"https://api.worldofwarships.{self.locale}/wows/account/info/?application_id={self.application_id}&account_id={pid}").content)["data"][str(pid)]
  def using_ships(self):
    resp=json.loads(requests.get(f"https://api.worldofwarships.asia/wows/ships/stats/?application_id={self.application_id}&account_id={self.account_id}").content)["data"][str(self.account_id)]
    self.usingships=resp
    return resp
  def get_rate(self):
    if not self.usingships:
      self.using_ships()
    types={}
    nations={}
    for ship in self.usingships:
      sh=Ship(self.application_id,ship["ship_id"]).value["details"]
      if sh["type"] in types:
        types[sh["type"]][sh["name"]]=ship["battles"]
      else:
        types[sh["type"]]={sh["name"]:ship["battles"]}
      if sh["nation"] in nations:
        nations[sh["nation"]]+=ship["battles"]
      else:
        nations[sh["nation"]]=ship["battles"]
        self.draw={"type":types,"nation":nations}
    return {"type":types,"nation":nations}
  def generate_figure(self,path):
    if not self.draw:
      self.get_rate()
    types=self.draw["type"]
    nations=self.draw["nation"]
    fig=plt.figure()
    ax1=fig.add_subplot(1,2,1)
    ax2=fig.add_subplot(1,2,2)
    x=[]
    n=[]
    labels=list(types.keys())
    for i in types:
      count=0
      for k in types[i]:
        count+=types[i][k]
      x.append(count)
    percent=["{:.1f}".format(i*100/sum(x)) for i in x]
    ax1.pie(x, startangle=90, counterclock=False,  autopct='%.1f%%', pctdistance=0.7)
    ax1.legend([f"{i}:{j}%" for i,j in zip(labels,percent)],loc="lower left",frameon=False,fontsize=7)
    for i in nations:
      n.append(nations[i])
    per=["{:.1f}".format(i*100/sum(n)) for i in n]
    label=list(nations.keys())
    ax2.pie(n,startangle=90, counterclock=False,  autopct='%.1f%%', pctdistance=0.7)
    ax2.legend([f"{i}:{j}%" for i,j in zip(label,per)],loc="lower left",frameon=False,fontsize=7)
    plt.savefig(path)
    