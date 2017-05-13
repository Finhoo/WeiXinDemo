# -*- coding:utf8 -*-

import web
import os
import hashlib
import reply
import receive
import time
from lxml import etree
from talk import talk
from image import img
from yanzhi import yanzhi

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class WeixinInterface:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, "tmplates")
        self.render = web.template.render(self.templates_root)
    def GET(self):
        data = web.input()
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        token = "wxpython"  # 请按照公众平台官网\基本配置中信息填写

        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        print "handle/GET func: hashcode, signature: ", hashcode, signature
        if hashcode == signature:
            return echostr
        else:
            return ""
    def POST(self):
           try:
               webData = web.data()
               xml = etree.fromstring(webData)
               print "Handle Post webdata is ", webData  # 后台打日志

               recMsg = receive.parse_xml(webData)
               toUser = recMsg.FromUserName
               fromUser = recMsg.ToUserName
               userid = toUser[0:10]
               if recMsg.MsgType == 'text':
                   content = talk(recMsg.Content, userid)
                   replyMsg = reply.TextMsg(toUser, fromUser, content)
                   return replyMsg.send()
               elif recMsg.MsgType == 'image':
                   mediaId = recMsg.MediaId
                   picUrl = xml.find('PicUrl').text
                   # result = img(picUrl)
                   # gender = result['gender']
                   # age = result['age']
                   # sex = '男'
                   # if gender == 'Female':
                   #     sex = '女'
                   # text = u"图中人物性别为" + sex + ', ' + u'年龄为' + age
                   yz = yanzhi(picUrl)
                   replyMsg = reply.TextMsg(toUser, fromUser, yz)
                   return replyMsg.send()
               else:
                   print "暂且不处理"
               return ''
           except Exception, Argment:
               print 'error'
               print Argment
               return ''

# def POST(self):
#     str_xml = web.data()
#     xml = etree.fromstring(str_xml)
#     msgType = xml.find('MsgType').text
#     fromUser = xml.find('FromUserName').text
#     toUser = xml.find('ToUserName').text
#     if msgType == 'text':
#         content = xml.find('Content').text
#         return self.render.reply_text(fromUser, toUser, int(time.time()), content)





