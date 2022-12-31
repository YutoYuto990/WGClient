from wows import wows
import json
import requests
import os

api=os.getenv("wows_api")

app=wows.App(api,"ja")
print(app.get_ship("Sinop").value)



#https://api.worldoftanks.asia/wot/auth/login/?application_id=