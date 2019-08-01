# -*- coding: UTF-8 -*-
import requests

def get(url,params,files):
    return requests.get(url, params=params, headers=files)

def getJson(url,params,files):
    return requests.get(url, params=params, headers=files)

def postJson(url,params,files):
    return requests.post(url, json=params, headers=files)

def putJson(url,params,files):
    return requests.put(url, json=params, headers=files)

def post(url,files):
    return requests.post(url, files=files)

