## ToDo list

- [ ] Control lighting based on the sun and gps location
- [ ] Turn off all devices (lights) when everyone leaves home
- [ ] Notify if there is motion in house when no one is home
- [ ] Lighting flashing when someone rings the doorbell
- [ ] install door/window sensors 
- [ ] install motion sensors
- [ ] Setup Motion Controlled Lights
- [ ] Investigate, install and configure new Xiaomi Hub and components
  - [ ] Xiaomi Hub
  - [ ] Xiaomi Smart Door Sensors
  - [ ] Xiaomi Smart Human Body Sensors
  - [ ] Xiami Smart Wireless Switch
- [ ] Setup and wallmount Android Tablet with Dashboard
  - [ ] Add a guest mode to the dashboard
- [ ] Build own Floorplan with additional functionality (I'm working on it)
- [ ] Implement Guest mode to disable certain interior automations
- [ ] Implement lights to be turned off if no one is home and no motion detection
- [ ] Setup Night and Day theme - Also apply to Floorplan
- [ ] Adding the chromecasts that are in the house (I'm working on it)
- [ ] Make a smart mirror and integrate it
- [ ] Make it possible to control the blinds
- [ ] Operate the garden lighting

- [ ] Convince everyone that Home Automation is the best!

## Big project - restructure folders, files and code
- [x] Remap the google assistant cloud component
- [x] Remap the lights component
- [x] Remap the device tracker component
- [x] Remap the rfxtrx and ifttt component
- [x] Remap the switches component from config.yaml
- [x] Remap the history and logbook component

## Already working (automation)

- [x] Sending telegram message if a door is open
- [x] Sending telegram message if phone battery level is under 25% (at the moment this is disabled)
- [x] Notification when there is a new update from HA
- [x] Reading weather info from Buienradar
- [x] Sending telegram message if a z-wave sensor had low battery
- [x] Sending telegram message if smoke sensor detect fire
- [x] Use an SSL certificate for extra security and sensor to show how many days to expire
- [x] Sending telegram message if it starts to rain within a hour
- [x] Send notifications for package delivery (PostNL)
- [x] Operate the water fountain
- [x] Purchase Google assistant and integrate it
- [x] Make use of WOL and turn on computers via home assistant
- [x] Start to using the new UI: LoveLace
- [x] Google calendar integration
- [x] Write data to an external database. This also speeds up the collection process in the log and history tab
- [x] Commit to github by filling in a text box and pressing the button, so easily!
- [x] Integration with Uptime Robot, so I get notified when the Pi is down.
- [x] Integration with Travis Ci.

- Analytics 
	- [x] Reading the battery percentages of all Z-wave devices 
	- [x] Show info about up and download speed
	- [x] Show info about the system version of Hassbian
	- [x] Show info about installed python version
	- [x] Show info about CPU performance
	- [x] Show info about storage from some files and how many percent is still available on the micro sd card
	- [x] Show info about how many days it will take until the SSL certificate expires
	- [x] Show info about the battery percent of Z-wave devices
	- [x] Show info about temperatures in the house