import json
import os
from datetime import datetime, timedelta
try:
    import requests
except ImportError:
    pass


class Connect():
    '''
    LoL
    '''
    def __init__(self, api_key=None):
          self.api_key = api_key
          self.base = 'http://antispaminc.tk/'
          if api_key is None:
              raise ApiError("You must supply a valid AntispamInc Api Key, Contact @AntispamIncBot To Get One")
    
