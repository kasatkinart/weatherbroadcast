import eel
from pyowm import OWM
import requests

owm = OWM("42e030774f81197c58b2ab8d8af8d59d")


@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    humidity = w.humidity
    clouds = w.detailed_status
    wind = w.wind
    print(wind)
    return 'В городе ' + place + ' сейчас: ' + str(temp) + '°С. ' + "Влажность составляет " + str(humidity) + "%. " + "Облачность: " + str(clouds)


eel.init('web')

eel.start('main.html', size=(700, 700))
