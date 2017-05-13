# -*- coding:utf8 -*-

import requests
import base64
import json
import time
import re

def yanzhi(url):
    im = base64.b64encode(requests.get(url).content)
    url = 'https://kan.msxiaobing.com/Api/Image/UploadBase64'
    r = requests.post(url, data=im)
    j = json.loads(r.content)
    url2 = 'https://kan.msxiaobing.com/Api/ImageAnalyze/Process?service=yanzhi&tid=4ecf1eb019cd4e0d8871f25a983bf9c2'
    img_url = j['Host']+j['Url']
    data = {
        "Content[imageUrl]": img_url,
        "CreateTime": time.time(),
    }
    r2 = requests.post(url2, data=data)
    result = re.search('{"text":"(.*?)",', r2.content).group(1)

    return result

# yanzhi('http://mmbiz.qpic.cn/mmbiz_jpg/thULgI0K2EtCbMd2hPtwZXYkzdOoiaptGsd73Q6PaM0x2Rp0KrSzXK9SgLVfickiaLNM7NhrNI2P90cnEQlx64cqQ/0')

