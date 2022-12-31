from .exception import *
from .utility.utils import get_json
class Arena:
  def __init__(self,application_id,lang,name=None):
    self.application_id=application_id
    self.lang=lang
    self.value=self._get_arena(name)
    
  def _get_arena(self,name=None):
    data=get_json(self.application_id,"encyclopedia/battlearenas",language=self.lang)
    res=None
    if not name:
      return data
    else:
      for i in data["data"]:
        if data["data"][i]["name"]==name:
          res=data["data"][i]
          break
        else:
          continue
      if res:
        return res
      else:
        raise ArenaNotFound("arena not found")