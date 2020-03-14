import pyowm


city = input('Город?: ')
# Москва
owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc')

#observation = owm.daily_forecast(city)
#w = observation.get_weather()
#temperature = w.get_temperature('celsius')['temp']


fc1 = owm.daily_forecast(city, limit=10)
f = fc1.get_forecast()
dayss = []
for weather in f:
    dayss.append('в ' + str(weather.get_reference_time('iso')[0:10]) + '  ' + str(weather.get_temperature('celsius')['day']))

print(dayss)