#coding: UTF-8
import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to


@respond_to('hello$', re.IGNORECASE)
def hello_reply(message):
    message.reply('hello sender!')


@respond_to('^reply_webapi$')
def hello_webapi(message):
    message.reply_webapi('hello there!', attachments=[{
        'fallback': 'test attachment',
        'fields': [
            {
                'title': 'test table field',
                'value': 'test table value',
                'short': True
            }
        ]
    }])


@respond_to('^reply_webapi_not_as_user$')
def hello_webapi_not_as_user(message):
    message.reply_webapi('hi!', as_user=False)


@respond_to('hello_formatting')
def hello_reply_formatting(message):
    # Format message with italic style
    message.reply('_hello_ sender!')


@listen_to('hello$')
def hello_send(message):
    message.send('hello channel!')


@listen_to('hello_decorators')
@respond_to('hello_decorators')
def hello_decorators(message):
    message.send('hello!')

@listen_to('hey!')
def hey(message):
    message.react('eggplant')


@respond_to(u'你好')
def hello_unicode_message(message):
    message.reply(u'你好!')


@listen_to('start a thread')
def start_thread(message):
    message.reply('I started a thread', in_thread=True)

@respond_to('say hi to me')
def direct_hello(message):
    message.direct_reply("Here you are")

import subprocess
from subprocess import PIPE
from still import *
from slackbot.utils import download_file, create_tmp_file
import os

import time


@respond_to('cam')
def Cam_reply(message):
    message.reply('motion_on')
    subprocess.run("sudo motion", shell=True,)

@respond_to('off')
def Cam_reply(message):
    message.reply('motion_off')
    subprocess.run("sudo pkill -f motion", shell=True,)
    
@respond_to('still')
def Cam_reply(message):
    still()
    message.reply('still')
    
    
    message.channel.upload_file('still_f/data.png',"/home/pi/slack-bot/slackbot/still_f/data.png")
    time.sleep(1)
    subprocess.run("sudo rm -r /home/pi/slack-bot/slackbot/still_f/data.png", shell=True,)
@respond_to('state')
def Cam_reply(message):
    #message.reply('on/off')
    proc = subprocess.run("ps ax |grep -v grep |grep -o motion", shell=True,stdout=PIPE,stderr=PIPE, text=True)
    state = proc.stdout
    
    if  state in "motion":
        message.reply('motion is off')
        message.reply(state)
    else :
        message.reply('motion is on')
        message.reply(state)
