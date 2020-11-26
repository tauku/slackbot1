#coding: UTF-8
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import subprocess
from subprocess import PIPE
from still2 import *
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
        #message.reply(state)
    else :
        message.reply('motion is on')
        #message.reply(state)
