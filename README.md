# Dunaujvarosi-egyetem-skript-nyelvek-
Egyetemi beadandó feladatnak létrehozott Github oldal.

# Időjárás kijelző (Perlik Boldizsár AJA5UX)

## Hallgató
Perlik Boldizsár

## Neptunkód
AJA5UX

## Feladat leírása
Valós időjárás lekérő és kijelző alkalmazás Dunaújváros városához.
A program a wttr.in nyilvános API-t használja, Tkinter felületen mutatja az adatokat.

## Modulok és a modulokban használt függvények
- sajat_modul_PB.py
  - get_weather_PB(city)
  - format_weather_PB(data)
  - save_report_PB(data, filename)
- bemutatando_modul_pelda.py
  - convert_c_to_f(c)
  - feels_like(temp_c, humidity)
  - cloud_description(code)
- main.py
  - IdojarasAppPB osztály

## Osztály(ok)
- IdojarasAppPB (tartalmaz frissítés és eseménykezelés gombokat)

## Függőségek
- Python 3
- tkinter
- requests

## Telepítés
```bash
pip install -r requirements.txt
python main.py
```
