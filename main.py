from wows import *
import json
import requests
import os

api=os.getenv("wows_api")

app=App(api,"ja",True)
print(app.get_ship("Sinop").value.details.name)



#https://api.worldoftanks.asia/wot/auth/login/?application_id=