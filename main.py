from wows import wows
import json
import requests
import os
import matplotlib.pyplot as plt

api=os.getenv("wows_api")
app=wows.App(api)
print(app.get_player("ziruconoob").save_fig("wows.png"))
"""
for ship in wows.get_player_ships("asia","ziruconoob"):
  sh=wows.get_ship_data(ship["ship_id"])["details"]
  if sh["type"] in val:
    val[sh["type"]][sh["name"]]=ship["battles"]
  else:
    val[sh["type"]]={sh["name"]:ship["battles"]}
print(val)
x=[]
labels=list(val.keys())
for i in val:
  m=0
  for k in val[i]:
    m+=val[i][k]
  x.append(m)
plt.pie(x, startangle=90, counterclock=False,  autopct='%.1f%%', pctdistance=0.8, labels=labels)
plt.savefig("wows.png")"""


#https://api.worldoftanks.asia/wot/auth/login/?application_id=