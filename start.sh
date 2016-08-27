#!/bin/sh

COMMAND=sudo python /home/pi/Slack-Bell-Bot/slack_bot.py
LOGFILE=restart.txt

writelog() {
  now=`date`
  echo "$now $*" >> $LOGFILE
}

writelog "Starting"
while true ; do
  $COMMAND
  writelog "Exited with status $?"
  writelog "Restarting"
  sleep 1s
done
