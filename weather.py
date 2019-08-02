import pyowm
#https://github.com/csparpa/pyowm
city = input("Ваш город:    ")
owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language='ru') #Your language
observation = owm.weather_at_place(city)

w = observation.get_weather()
temperature=w.get_temperature('celsius')['temp']
humidity=w.get_humidity()
speedWind=w.get_wind()["speed"]

print("В " + city +"е сейчас " + w.get_detailed_status()) #weather
print("Сейчас температура: " + str(temperature) + " по Цельсию.")  #temperature
print("Влажность = "+ str(humidity)) #humidity
print('Скорость ветра = '+str(speedWind)) #speed wind
