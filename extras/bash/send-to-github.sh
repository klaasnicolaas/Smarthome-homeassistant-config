#!/bin/bash
cd /home/homeassistant/.homeassistant
git add .
git commit -a -m "Update with the button"
git push origin master
exit