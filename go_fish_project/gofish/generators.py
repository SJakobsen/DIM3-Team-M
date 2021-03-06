from random import randint
from math import floor
from random import gauss

worldWidth = 20
worldHeight = 16

def generateLake():
    lake = []
    # fill in the lake with ones
    for i in range(0, worldHeight):
        lake.append([])
    for i in range(0, worldHeight):
        for j in range(0, worldWidth):
            lake[i].append(1)

    # make holes
    for i in range(0, randint(5,15)):
        makeHole(lake, worldWidth, worldHeight)

    return lake

def makeHole(lake, w, h):
    # choose the pit
    x = randint(1, w-2)
    y = randint(1, h-2)

    # choose the depth
    d = randint(5, 10)
    if (d > 10):
        d = 10

    # start spreading the hole
    digDown(lake, d, x, y, w, h)

def digDown(lake, d, x, y, w, h):
    if x < 0 or y < 0 or x >= w or y >= h:
        return
    if lake[y][x] >= d:
        return
    lake[y][x] = d
    digDown(lake, nextDepth(d), x, y-1, w, h)
    digDown(lake, nextDepth(d), x+1, y, w, h)
    digDown(lake, nextDepth(d), x, y+1, w, h)
    digDown(lake, nextDepth(d), x-1, y, w, h)

def nextDepth(d):
    return d - randint(0, 2)

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
    
def perceivedDepth(hour, depth):
    '''
    6 7 8 9 10 11 12 13 14 15 16 17
    0 1 2 3 4  5  6  7  8  9  10 11
    0 1 2 3 4  5  6  5  4  3  2  1
    '''
    absHour = hour
    if absHour > 6:
        absHour = absHour - (absHour - 6)
    modDepth = depth - absHour/2
    pDepth = -1
    if modDepth >= 7:
        pDepth = 3
    elif modDepth >= 4:
        pDepth = 2
    elif modDepth >= 1:
        pDepth = 1
    else:
        pDepth = 0
    '''
    6 >= 10 = 3
    0 >= 7  = 3
    6 >= 7  = 2
    0 >= 4  = 2
    6 >= 4  = 1
    0 >= 1  = 1
    6 >= 1  = 0
    '''
    return pDepth

def perceivedWindyness(windms):
    if windms < 5:
        return 0
    if windms < 11:
        return 1
    return 2

