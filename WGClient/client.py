from .wows import WowsApp
from .exception import *


class Client:

    def __init__(self, application_id, lang, conv=False):
        if not isinstance(application_id, str):
            raise InvalidApplicationId("invalid application id provided.")
        self.wows = WowsApp(application_id, lang, conv)
