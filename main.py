import wows
from dictionary import Dict
import json
import requests
import os
import matplotlib.pyplot as plt
wows=wows.Wows()
api=os.getenv("wows_api")
val={}

for ship in wows.get_player_ships("asia","googlecom_accurate"):
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
plt.savefig("wows.png")


#https://api.worldoftanks.asia/wot/auth/login/?application_id=