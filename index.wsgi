# -*- coding:utf8 -*-
import os
import hashlib
import web
import lxml
import time
import urllib2,json
from lxml import etree
import sae
from weixin import WeixinInterface
sae.add_vendor_dir('vendor')

urls=(
'/wx','WeixinInterface'
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root,'templates')
render = web.template.render(templates_root)
app = web.application(urls, globals()).wsgifunc()
application=sae.create_wsgi_app(app)