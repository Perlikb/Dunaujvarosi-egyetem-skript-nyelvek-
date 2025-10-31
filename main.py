from tkinter import Tk, Label, Button, StringVar, W, E
from sajat_modul_PB import get_weather_PB, format_weather_PB
from bemutatando_modul_pelda import convert_c_to_f, feels_like, cloud_description

class IdojarasAppPB:
    def __init__(self, root):
        self.root = root
        self.root.title("Időjárás kijelző - Dunaújváros")
        self.city_var = StringVar()
        self.temp_var = StringVar()
        self.cond_var = StringVar()
        self.hum_var = StringVar()
        self.wind_var = StringVar()
        self.city_var.set("Város: Dunaújváros")

        Label(root, textvariable=self.city_var, font=("Arial", 14)).grid(row=0, column=0, columnspan=2, sticky=W)
        Label(root, textvariable=self.temp_var, font=("Arial", 24)).grid(row=1, column=0, columnspan=2, sticky=W)
        Label(root, text="Feltételek:").grid(row=2, column=0, sticky=W)
        Label(root, textvariable=self.cond_var).grid(row=2, column=1, sticky=W)
        Label(root, text="Páratartalom:").grid(row=3, column=0, sticky=W)
        Label(root, textvariable=self.hum_var).grid(row=3, column=1, sticky=W)
        Label(root, text="Szél:").grid(row=4, column=0, sticky=W)
        Label(root, textvariable=self.wind_var).grid(row=4, column=1, sticky=W)

        Button(root, text="Frissít", command=self.refresh).grid(row=5, column=0, sticky=E)
        Button(root, text="Kilép", command=root.quit).grid(row=5, column=1, sticky=W)

        self.refresh()

    def refresh(self):
        data = get_weather_PB("Dunaújváros")
        self.temp_var.set(format_weather_PB(data))
        self.cond_var.set(cloud_description(data["clouds"]))
        self.hum_var.set(f'{data["humidity"]} %')
        self.wind_var.set(f'{data["wind_kmh"]} km/h, érzet: {feels_like(data["temp_c"], data["humidity"])} °C')

if __name__ == "__main__":
    root = Tk()
    app = IdojarasAppPB(root)
    root.mainloop()
