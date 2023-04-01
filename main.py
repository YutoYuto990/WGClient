from WGClient import Client
import os

api=os.getenv("wows_api")

client=Client(api,"ja")
user=client.wows.get_clan("WTN")
print(user)



#https://api.worldoftanks.asia/wot/auth/login/?application_id=