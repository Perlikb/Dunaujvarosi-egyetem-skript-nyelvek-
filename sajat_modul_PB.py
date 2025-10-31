import requests

def get_weather_PB(city="Dunaújváros"):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        r = requests.get(url, timeout=5)
        data = r.json()
        current = data["current_condition"][0]
        temp_c = float(current["temp_C"])
        humidity = int(current["humidity"])
        wind_kmh = int(current["windspeedKmph"])
        condition = current["weatherDesc"][0]["value"]
        clouds = "cloudy" if "cloud" in condition.lower() else "clear"
        return {"city": city, "temp_c": temp_c, "humidity": humidity, "wind_kmh": wind_kmh, "condition": condition, "clouds": clouds}
    except Exception as e:
        return {"city": city, "temp_c": 0, "humidity": 0, "wind_kmh": 0, "condition": "N/A", "clouds": "clear"}

def format_weather_PB(data):
    return f'{data["temp_c"]} °C - {data["condition"]}'

def save_report_PB(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(data))
    return filename
