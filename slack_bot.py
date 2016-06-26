import time
import os
from slackclient import SlackClient

# Insert you bots token
BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
# What channel your bot uses
CHANNEL_NAME = "general"

def main():
    # Creates a slackclient instance with bots token
    sc = SlackClient(BOT_TOKEN)
    
    #Connect to slack
    if sc.rtm_connect():
        
        while True:
            # Read latest messages
            for slack_message in sc.rtm_read():
                message = slack_message.get("text")
                user = slack_message.get("user")
                if not message or not user:
                    continue
                # If someone types ring, the bot will post a bell
                if(message == "ring"):
                    sc.rtm_send_message(CHANNEL_NAME, ":bell:")
                    
            # Sleeps for one second
            time.sleep(1)


if __name__ == '__main__':
    main()
