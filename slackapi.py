# -*- coding: UTF-8 -*-
import api

CHANNEL = "#test"
USER_NAME_ENTRY = "Card Entry now."
USER_NAME_EXIT =  "Card Exit now."
USER_NAME_KIGEN = "Card kigen Gire!!!."
URL = "https://hooks.slack.com/services/"
API_KEY = "TCW4RRVKQ/BK88X72HY/BAp8jy2jmRATotaBIzRV3eXi"

def entry(memberId, entryDate, output):
    api.post(URL + API_KEY, {'payload': (None, '{"channel":"'+ CHANNEL +'", "username":"'+ USER_NAME_ENTRY +'", "text":"'+ output +'", "icon_emoji": ":watch:"}'),})

def out(memberId, entryDate, output):
    api.post(URL + API_KEY, {'payload': (None, '{"channel":"'+ CHANNEL +'", "username":"'+ USER_NAME_EXIT +'", "text":"'+ output +'", "icon_emoji": ":watch:"}'),})

def kigen(memberId, entryDate, output):
    api.post(URL + API_KEY, {'payload': (None, '{"channel":"'+ CHANNEL +'", "username":"'+ USER_NAME_KIGEN +'", "text":"'+ output +'", "icon_emoji": ":ghost:"}'),})