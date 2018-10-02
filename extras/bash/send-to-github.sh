#!/bin/bash
####################################
## This script pushes my selected ##
## files to my github repo on a   ##
## new branch called 'master'     ##
####################################
sudo -u homeassistant -H -s
cd /home/homeassistant/.homeassistant/
git add .
git commit -a -m "Update with the button"
git push origin master
exit