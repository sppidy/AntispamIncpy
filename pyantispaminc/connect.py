# Copyright (C) 2020 AntiSpam, Inc. <http://antispaminc.tk/>
#
#                    GNU GENERAL PUBLIC LICENSE
#                      Version 3, 29 June 2007

# Copyright (C) 2020 AntiSpam, Inc. <http://antispaminc.tk/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

import json
import os
from datetime import datetime, timedelta
import requests
from .class_types import Antispamclass

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
            return Antispamclass(**seds)

class ApiError(Exception):
    pass
