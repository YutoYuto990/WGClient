from .exception import *
from .utility.utils import get_json

class Ship:
  def __init__(self,
               application_id,
               conv,
               lang,
               name_or_id):
    self.conv=conv
    self.lang=lang
    self.application_id=application_id
    if isinstance(name_or_id,int):
      self.id=name_or_id
    else:
      self.id=self._get_ship_id(name_or_id)
    self.value=self.conv(self._get_ship_data())
    self.origin=self._get_ship_data()
  
  def _get_ship_id(self,name):
    for i in range(1,100):
      ships=get_json(self.application_id,"encyclopedia/ships",page_no=i,language=self.lang)
      for sh in ships["data"]:
        if ships["data"][sh]["name"]==name:
          return sh
    raise ShipNotFound("ship not found")

  def _get_ship_data(self):
      sid=self.id
      details=get_json(self.application_id,"encyclopedia/ships",ship_id=sid,language=self.lang)["data"][str(sid)]
      data=get_json(self.application_id,"encyclopedia/shipprofile",ship_id=sid,language=self.lang)
      data["data"][str(sid)]["details"]=details
      return data["data"][str(sid)]
  