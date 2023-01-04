from .wows import WowsApp
class Client:
  def __init__(self,application_id,lang,conv=False):
    self.application_id
    self.wows=WowsApp(application_id,lang,conv)