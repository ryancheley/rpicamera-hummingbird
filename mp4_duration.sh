#!/bin/sh
echo "Logging Video Duration" >> /home/pi/Documents/python_projects/log.txt
MyDate="`date +'%m/%d/%Y, %H:%M, '`"
MyDur="`ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 hummingbird.mp4`"
echo "$MyDate$MyDur" >> /home/pi/Documents/python_projects/duration.txt