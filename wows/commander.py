from .exception import *
from .utility.utils import get_json

class Commander:
  def __init__(self,
               application_id,
               conv,
               lang,
               name=None):
    self.application_id=application_id
    self.lang=lang
    self.value=self._get_commander_info(name)
    
  def _get_commander_id(self,name):
    res=get_json(self.application_id,"encyclopedia/crews",language=self.lang)["data"]
    cid=None
    for commander_id in res:
      if name in res[commander_id]["first_names"]:
        cid=int(commander_id)
        break
      else:
        continue
    if cid:
      self.commander_id=cid
      return cid
    else:
      raise CommanderNotFound("commander not found.")
  
  def _get_commander_info(self,name_or_id):
    if name_or_id:
      if isinstance(name_or_id,int):
        self.commander_id=name_or_id
        res=get_json(self.application_id,"encyclopedia/crews",language=self.lang,commander_id=name_or_id)
      else:
        res=get_json(self.application_id,"encyclopedia/crews",language=self.lang,commander_id=self._get_commander_id(name_or_id))
    else:
      res=get_json(self.application_id,"encyclopedia/crews",language=self.lang)
    res["data"][str(self.commander_id)]["id"]=self.commander_id
    return res["data"][str(self.commander_id)]