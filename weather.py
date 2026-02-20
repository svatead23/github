import urequests

def get_location():
    r = urequests.get("http://ip-api.com/json")
    data = r.json()
    r.close()
    return data["lat"], data["lon"]

def get_weather(lat, lon, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    r = urequests.get(url)
    data = r.json()
    r.close()

    return {
        "temp": round(data["main"]["temp"]),
        "desc": data["weather"][0]["main"]
    }