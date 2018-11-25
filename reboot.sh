#!/bin/sh

echo "Reboot command sent at $(date)" >> log.txt

sudo /sbin/shutdown -r +5
