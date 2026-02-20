# Weather Station – Raspberry Pi Pico W

## Popis

Stanice zobrazuje počasí a čas na I2C LCD displeji.

## Zapojení

LCD → Pico W (I2C):

* SDA → GPIO 0
* SCL → GPIO 1
* VCC → 3.3V
* GND → GND

## Instalace

1. Nahrajte MicroPython do Pico W
2. Nahrajte všechny soubory
3. Upravte config.json
4. Spusťte main.py

## Funkce

* Automatické WiFi připojení
* Zjištění lokace přes IP
* Počasí z OpenWeatherMap
* NTP čas
* Aktualizace každých 10 minut
