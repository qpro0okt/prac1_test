import eel
import pyowm

own = pyowm.OWM('879f53ba02fe001c6831425a7efeab74')


@eel.expose
def get_weather(place):
    mgr = own.weather_manager()

    observation = mgr.weather_at_place(place)
    w = observation.weather

    temp = w.temperature('celsius')['temp']

    return "В городе " + place + " сейчас " + str(temp) + " градусов"
    
eel.init("G:/python_projects/web")

eel.start('main.html', size=(700, 700))

