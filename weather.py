import pyowm

city = input("Your city:    ")
owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language='ru') #Your language
observation = owm.weather_at_place(city)

w = observation.get_weather()
temperature=w.get_temperature('celsius')['temp']
humidity=w.get_humidity()
speedWind=w.get_wind()["speed"]

print("In " + city +" now " + w.get_detailed_status()) #weather
print("The temperature is: " + str(temperature))  #temperature
print("Humidity = "+ str(humidity)) #humidity
print('Speed wind = '+str(speedWind)) #speed wind
