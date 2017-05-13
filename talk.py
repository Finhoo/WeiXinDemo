# -*- coding:utf8 -*-

import requests
import json

def talk(content, userid):
    url = "http://www.tuling123.com/openapi/api"
    s = requests.session()
    d = {"key": "ea754fdd1c6544fda50a7785723475da", "info": content, "userid": userid}
    data = json.dumps(d)
    r = s.post(url, data=data)
    text = json.loads(r.text)
    code = text["code"]
    if code == 100000:
        result = text['text']
    elif code == 200000:
        result = text['text'] + '\n' + text['url']
    elif code == 302000:
        result = text['text'] + '\n' +text['list'][0]['article'] + '\n' + text['list'][0]['detailurl']
    elif code == 308000:
        result = text['text'] + '\n' + text['list'][0]['name'] + '\n' + text['list'][0]['info'] + '\n' + text['list'][0]['detailurl']
    else: result = ''
    return result

# print talk(u"新闻", 100000)


