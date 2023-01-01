from wows import *
import json
import requests
import os

api=os.getenv("wows_api")

app=App(api,"ja")
print(app.get_commander(3854739152).value)



#https://api.worldoftanks.asia/wot/auth/login/?application_id=