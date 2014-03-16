from random import randint
from random import gauss

def generateWeather():
	weatherSet = []
	for i in range(12):
		weatherList = {}
		rain = 0
		windms = -1
		winddir = -1
		temp = -1
		
		clouds = randint(0,2)
		weatherList['clouds'] = clouds
		
		if clouds != 0:
			rain = randint(1,2)
		weatherList['rain'] = rain
		
		windms = gauss(8+rain+clouds,2+rain)
		weatherList['windms'] = windms
		
		winddir = randint(0,3)
		weatherList['winddir'] = winddir
		
		temp = randint(10,25)
		weatherList['temp'] = temp

		weatherSet.append(dict(weatherList))
	return weatherSet