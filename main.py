import time
import json
from machine import I2C, Pin

from lcd_i2c import Lcd_i2c
from wifi import connect_wifi, ensure_wifi
from weather import get_location, get_weather
from ntp_time import sync_time, get_time_str

# I2C setup pro LCD
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)
lcd = Lcd_i2c(i2c)

def lcd_show(line1="", line2=""):
    lcd.clear()
    lcd.set_cursor(0, 0)
    lcd.write(line1[:16])
    lcd.set_cursor(0, 1)
    lcd.write(line2[:16])

# načtení configu
with open("config.json") as f:
    config = json.load(f)

# WiFi připojení
lcd_show("Connecting...", "WiFi")
connect_wifi(config["wifi_ssid"], config["wifi_password"])

# čas
sync_time()

# lokalita
lat, lon = get_location()
lcd_show("Location:", f"{lat:.2f},{lon:.2f}")
time.sleep(4)

last_update = 0
weather = {"temp": "--", "desc": "Loading"}

while True:
    ensure_wifi(config["wifi_ssid"], config["wifi_password"])

    if time.time() - last_update > 600:
        try:
            weather = get_weather(lat, lon, config["openweather_api_key"])
            last_update = time.time()
        except:
            lcd_show("Weather API", "ERROR")
            time.sleep(5)
            continue

    time_str = get_time_str()
    line1 = f"{time_str} {weather['temp']}C"
    line2 = weather["desc"]

    lcd_show(line1, line2)
    time.sleep(1)