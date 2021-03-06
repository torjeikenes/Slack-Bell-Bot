#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import os
from slackclient import SlackClient

# Insert you bots token
BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
# What channel your bot uses
CHANNEL_NAME = "sales-bell"

def servo():
    # Sets up GPIO
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(7,GPIO.OUT)

    p = GPIO.PWM(7,50)
    p.start(7.5)

    # Rings bell 3 times
    for i in range(3):
        p.ChangeDutyCycle(10)
	time.sleep(0.25)

	p.ChangeDutyCycle(3)
	time.sleep(.25)
	
    p.ChangeDutyCycle(6)
    time.sleep(0.5)
	
    p.stop()
    GPIO.cleanup()

def main():
    # Creates a slackclient instance with bots token
    sc = SlackClient(BOT_TOKEN)
    
    #Connect to slack
    if sc.rtm_connect():
        print "connected" 
        while True:
            # Read latest messages
            for slack_message in sc.rtm_read():
                message = slack_message.get("text")
                user = slack_message.get("user")
                if not message or not user:
                    continue
                # If someone types ring, the bot will post a bell
                if(message.lower().strip() == "ring"):
                    sc.rtm_send_message(CHANNEL_NAME, ":bell:")
                    servo() 
            # Sleeps for one second
            time.sleep(1)

while True:
    if __name__ == '__main__':
        main()
