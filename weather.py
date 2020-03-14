import pyowm, json, time

""" CREATE FILE """
timestr = time.strftime("%Y%m%d")
filename = timestr + ".json"
myfile = open(filename, mode='w', encoding='Latin-1')

city = input('Город?: ')
# Москва & Moscow
owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc')
fc1 = owm.daily_forecast(city, limit=10)
f = fc1.get_forecast()
dayss = []
for weather in f:
    dayss.append('Date: ' + str(weather.get_reference_time('iso')[0:10]) + '  celsius: ' + str(weather.get_temperature('celsius')['day']))

""" SAVE JSON FILE """
json.dump(dayss, myfile)
myfile.close()