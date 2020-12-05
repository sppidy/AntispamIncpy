import json
import os
from datetime import datetime, timedelta
import requests
from class_types import anc

class Antispaminc():
    '''
    LoL
    '''
    def __init__(self, token=None):
          self.token = token
          self.base = 'http://antispaminc.tk/'
          if token is None:
              raise ApiError("You must supply a valid AntispamInc Api Key, Contact @AntispamIncBot To Get One")
    
    def is_banned(self, user_id):
          token = self.token  
          userid = user_id
          is_it = {
              'token': token,
              'userid': userid
          }
          urlz = self.base + '/info/'
          seds = requests.post(url=urlz, data=is_it).json()
          if seds['error'] == True:
                raise ApiError('Something Went Wrong. \nError' + seds['full'])
          else:
                lol = seds['banned']
                return lol
        
    def reason_s(self, user_id):
          token = self.token  
          userid = user_id
          is_it = {
              'token': token,
              'userid': userid
          }
          urlz = self.base + '/info/'
          seds = requests.post(url=urlz, data=is_it).json()
          if seds['error'] == True:
                raise ApiError('Something Went Wrong. \nError' + seds['full'])
          else:
                lol = seds['reason']
                return anc(lol)
          
