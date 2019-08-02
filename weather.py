import pyowm
#https://github.com/csparpa/pyowm
city = input("Ваш город:    ")
owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language='ru')
observation = owm.weather_at_place(city)

w = observation.get_weather()
temperature=w.get_temperature('celsius')['temp']
humidity=w.get_humidity()
speedWind=w.get_wind()["speed"]

print("В " + city +"е сейчас " + w.get_detailed_status())
print("Сейчас температура: " + str(temperature) + " по Цельсию.")
print("Влажность = "+ str(humidity))
print('Скорость ветра = '+str(speedWind))
