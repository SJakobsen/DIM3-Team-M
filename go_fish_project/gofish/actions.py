from random import random
from random import randint
from math import *
from generators import *
from gofish.models import Bait, Fish

def doFishing(depth, weather, hour, bait, attemptNo):
    # get the perceived depth
    depth = perceivedDepth(hour, depth)

    # get all the fish
    fish = []
    for f in Fish.objects.all():
        fish.append(f)

    # choose the fish that we will be trying to catch
    f = fish[ randint(0, len(fish)-1) ]

    # calculate the chance of caching
    chance = f.base_chance
    # bait and depth modifiers can do both positive and negative impact
    chance += 10 - abs(f.p_depth - depth) * 10
    chance += 10 - abs(f.p_bsize - bait.size) * 10
    # cloudyness, windyness and rainyness can only add +5 if matched
    if (perceivedWindyness(weather['windms']) == f.p_wind):
        chance += 5
    if (weather['clouds'] == f.p_clouds):
        chance += 5
    if (weather['rain'] == f.p_rain):
        chance += 5;

    # applying the diminishing returns
    chance *= pow(0.9, (attemptNo-1))

    # cap the random
    if (chance < 0): chance = 0
    if (chance > 100): chance = 100 # though this line is redundant

    # if we have caught the fish
    if (randint(1, 100) <= chance):
        # generate a random point from the gaussian
        # I need it because I will use the same point
        # for length, weigth and price
        U1 = random(); U2 = random()
        Z1 = sqrt ((-2) * log (U1)) * cos (2 * 3.14159265 * U2);

        weight = round(float(f.weight_mean) + Z1 * float(f.weight_sd), 2)
        if (weight < 0.2):
            weight = 0.2

        size = round(float(f.size_mean) + Z1 * float(f.size_sd), 2)
        if (size < 10):
            size = 10

        price = round(float(f.base_price) + Z1 * float(f.base_price) / 2, 2)
        if (price < 5):
            price = 5

        # and we caught it!
        return { 'fish': f, 'weight': weight, 'size': size, 'price': price }

    return None

def moveTo(curX, curY, x, y, w, h, currTime):
    mfailed = { 'currentTime': currTime, 'status': 'uncool' }
    if (x < 0 or y < 0 or x >= w or y >= h):
        return mfailed
    timeNeeded = (abs(curX - x) + abs(curY - y)) * 0.2
    if (currTime + timeNeeded > 11.5):
        return mfailed
    return { 'currentTime': currTime + timeNeeded, 'status': 'ok' }
