#!/bin/bash
logfile="/tmp/my.log"
echo "$(date) ============ begin" >>"$logfile"
who >>"$logfile"
ps  >>"$logfile"
df >>"$logfile"
# other commands to investigate the environment >>"$logfile"
# ...
# your python command goes here. The `&>>` redirects STDOUT and STDERR. 
python3 /home/ec2-user/chatbot/src/discord_bot.py  &>>"$logfile"
status=$? 
echo "$(date) exit status: $status"  >>"$logfile"
exit $status 