def convert_c_to_f(c):
    return round((c * 9/5) + 32, 1)

def feels_like(temp_c, humidity):
    t = temp_c
    h = humidity
    feels = t - (h/100) * 5
    return round(feels, 1)

def cloud_description(code):
    if code == "clear":
        return "Tiszta égbolt"
    if code == "cloudy":
        return "Felhős égbolt"
    return "Ismeretlen"
