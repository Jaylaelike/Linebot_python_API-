#!/usr/bin/python
#-*-coding: utf-8 -*-
##from __future__ import absolute_import
###
from flask import Flask, jsonify, render_template, request
import json

#import pymongo
#from pymongo import MongoClient
#from flask_restful import Resource, Api, reqparse

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,ImageSendMessage, StickerSendMessage, AudioSendMessage
)
from linebot.models.template import *
from linebot import (
    LineBotApi, WebhookHandler
)

app = Flask(__name__)

lineaccesstoken = 'CJVcBKqaM55S2pmJq9VSi4b62QE5v2I1xcPBWehys0KuqEjtvRbJDjmJCVll5JlSHDhRXDGiTyBQTDfq8S8KHfOJbDW8aBCylHAYg+xjZEkqD7oj3M/LtjUJRaojas4MDmQVFeAs2nFn1lJT9IOq7wdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(lineaccesstoken)

####################### new ########################
@app.route('/')
def index():
    return "Hello World!"


@app.route('/joey', methods=['POST'])
def callback():
    #try:
    json_line = request.get_json(force=False,cache=False)
    #except:
    #    print('cannot get json_line')
    #    return '',200
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    no_event = len(decoded['events'])
    for i in range(no_event):
        event = decoded['events'][i]
        #try:
        event_handle(event)
        #except:
        #    pass
    return '',200


def event_handle(event):
    try:
        userId = event['source']['userId']
    except:
        print('error cannot get userId')
        return ''

    try:
        rtoken = event['replyToken']
    except:
        print('error cannot get rtoken')
        return ''
    try:
        msgId = event["message"]["id"]
        msgType = event["message"]["type"]
    except:
        print('error cannot get msgID, and msgType')
        sk_id = np.random.randint(1,17)
        replyObj = StickerSendMessage(package_id=str(1),sticker_id=str(sk_id))
        line_bot_api.reply_message(rtoken, replyObj)
        return ''
#
    if msgType == "text":
        msg = str(event["message"]["text"])
        outmsg = textmessagehandler(msg)
        replyObj = TextSendMessage(text=outmsg)
        line_bot_api.reply_message(rtoken, replyObj)

    else:
        replyObj = StickerSendMessage(package_id=str(1),sticker_id=str(sk_id))
        line_bot_api.reply_message(rtoken, replyObj)
    return ''

def testmessagehandler(msg):
    return msg

#if __name__ == '__main__':
#    app.run(threaded=True)
