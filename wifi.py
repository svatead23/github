import network
import time

wlan = network.WLAN(network.STA_IF)

def connect_wifi(ssid, password):
    wlan.active(True)
    wlan.connect(ssid, password)

    timeout = 15
    while not wlan.isconnected() and timeout > 0:
        time.sleep(1)
        timeout -= 1

def ensure_wifi(ssid, password):
    if not wlan.isconnected():
        connect_wifi(ssid, password)