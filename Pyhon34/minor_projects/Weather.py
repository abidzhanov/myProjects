import pyowm

owm = pyowm.OWM('abd87355f56eb653a68bc47b56c8a332')
city = input('Enter name of city: ')
print('Expample: temperature, wind, humidity, weather')
what = input('What would you like to know: ').lower()
observation = owm.weather_at_place(city)
w = observation.get_weather()

def printWeater(what, w):
	if what == 'weather':
		print(w)
	elif what == 'temperature':
		print(w.get_temperature('celsius'))
	elif what == 'wind':
		print(w.get_wind())
	elif what == 'humidity':
		print(w.get_humidity())

printWeater(what, w)
