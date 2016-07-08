#Slack Bell

## What you need
To use the bell you need the following:
* A raspberry pi, setup with ssh
* A servo motor
* A bell
 

## Installation

ssh to the raspberry

ssh pi@<ip>

cd
git clone https://github.com/torjeikenes/Slack-Bell-Bot
cd Slack-Bell-Bot
sudo pip install -r requirements.txt

Open slack_bot.py in you favorite text editor and change the CHANNEL_NAME to the channel
the bot will be in.

## Setup
create a slack bot and copy the token
Create an environment variable named SLACK_BOT_TOKEN and assign the token to it

Connect the positive wire to pin 4, the negative wire to pin 6, and the signal wire to pin 7
install tmux
sudo apt-get install tmux
open a tmux session by typing
tmux
in the tmux session type
python slack_bot.py
to start the script
to detatch from the session, press Ctrl+b followed by d
this will leave the script running in the background when you leave the 
type "Ring" in the specified slack channel and the bell will ring
