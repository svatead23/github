import ntptime
import time

def sync_time():
    try:
        ntptime.settime()
    except:
        pass

def get_time_str():
    t = time.localtime()
    return "{:02}:{:02}:{:02}".format(t[3], t[4], t[5])