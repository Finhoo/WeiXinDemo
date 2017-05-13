# -*- coding:utf8 -*-
import requests
import re

def img(url):
    im = requests.get(url).content
    url = 'https://how-old.net/Home/Analyze?isTest=False&source=&version=how-old.net'
    data = {'file': im}
    r = requests.post(url, files=data).content.replace('\\', '')
    gender = re.search(r'"gender": "(.*?)"rn', r).group(1)
    age = re.search(r'"age": (.*?),rn', r).group(1)
    print gender
    print age
    return {"age": age, "gender": gender}
# print img('http://mmbiz.qpic.cn/mmbiz_jpg/thULgI0K2EtCbMd2hPtwZXYkzdOoiaptGsd73Q6PaM0x2Rp0KrSzXK9SgLVfickiaLNM7NhrNI2P90cnEQlx64cqQ/0')
