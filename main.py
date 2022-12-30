from wows import wows
import json
import requests
import os
import matplotlib.pyplot as plt

api=os.getenv("wows_api")

app=wows.App(api)
print(app.get_player("googlecom_accurate").save_data("wows.png"))



#https://api.worldoftanks.asia/wot/auth/login/?application_id=