import os.path, time
print("%s" % time.ctime(os.path.getmtime("/home/homeassistant/.homeassistant/.git/index")))