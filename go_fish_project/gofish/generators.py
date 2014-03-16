from random import randint
from math import floor
from random import gauss

worldWidth = 20
worldHeight = 16

def generateLake():
    lake = []
    for i in range(0, worldWidth):
    	lake.append([])

    for i in range(0, worldWidth):
    	for j in range(0, worldHeight):
    		lake[i].append(floor(randint(1,10)))

    return lake

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
