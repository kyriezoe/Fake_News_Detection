#!/usr/bin/python3
#-*- coding:utf-8 -*-
from urllib import request,parse
import json

def __init__(self):
    pass

def setUrl(_url):
    global url
    url = _url

def setHeaders(_headers):
    global headers
    headers = _headers

def setParameter(_url,_headers):
    global url,headers
    url = _url
    headers = _headers

def init(_url="http://fakebox-219822.appspot.com/fakebox/check",\
    _headers={'Content-Type': 'application/json'}):
    setParameter(_url,_headers)

def inter_parse(res_json):
    title_decision = "unknown"
    if "decision" in res_json["title"]:
        title_decision = res_json["title"]["decision"]
    title_score = 0.0
    if "score" in res_json["title"]:
         title_score = res_json["title"]["score"]
    content_decision = "unknown"
    if "decision" in res_json["content"]:
        content_decision = res_json["content"]["decision"]
    content_score = 0.0
    if "score" in res_json["content"]:
         content_score = res_json["content"]["score"]
    rs = {
        "title_decision":title_decision,
        "title_score":title_score,
        "content_decision":content_decision,
        "content_score":content_score
    }
    return rs
    
def sendRequest3(_url,_title,_content):
    character_set = "utf-8"
    data ={
	    "url": _url,
	    "title": _title,
	    "content": _content
    }
    data = bytes( json.dumps(data) , character_set )
    req = request.Request(url=url,headers=headers,data=data)
    res = request.urlopen(req)#timeout=10sec?
    if res.getcode()!=200:return -1
    res_str = res.read().decode(character_set)
    res_json = json.loads(res_str)
    if not res_json["success"]: return -1
    res_ret = inter_parse(res_json)
    return res_ret

def sendRequest(_tuple):
    # print(_tuple[0],_tuple[1],_tuple[2])
    return sendRequest3(_tuple[0],_tuple[1],_tuple[2])

    
