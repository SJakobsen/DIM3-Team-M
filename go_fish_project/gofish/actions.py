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
    f = chooseRandomFish(fish, depth, weather, hour, bait)

    # calculate the chance of caching
    chance = getAccomodatedChance(f, depth, weather, hour, bait)

    # applying the diminishing returns
    chance *= pow(0.8, attemptNo)

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

        size = int(round(float(f.size_mean) + Z1 * float(f.size_sd), 2))
        if (size < 10):
            size = 10

        price = int(float(f.base_price) + Z1 * float(f.base_price) / 2)
        if (price < 5):
            price = 5

        # and we caught it!
        return { 'fish': f, 'weight': weight, 'size': size, 'price': price,
                'chance': chance, 'origChance': getAccomodatedChance(f, depth, weather, hour, bait) }

    return None

def getAccomodatedChance(f, depth, weather, hour, bait):
    chance = f.base_chance
    # bait and depth modifiers can do both positive and negative impact
    chance += 5 - abs(f.p_depth - depth) * 10
    chance += 5 - abs(f.p_bsize - bait.size) * 10
    # cloudyness, windyness and rainyness can only add +5 if matched
    if (perceivedWindyness(weather['windms']) == f.p_wind):
        chance += 5
    if (weather['clouds'] == f.p_clouds):
        chance += 5
    if (weather['rain'] == f.p_rain):
        chance += 5;
    if chance < 0:
        chance = 0
    return chance

def chooseRandomFish(fish, depth, weather, hour, bait):
    chance = 0;
    for f in fish:
        chance += getAccomodatedChance(f, depth, weather, hour, bait)
        print f.name, getAccomodatedChance(f, depth, weather, hour, bait)

    # generate random number from the whole probability distribution
    rnd = randint(1, chance)
    n = 0
    for f in fish:
        n += getAccomodatedChance(f, depth, weather, hour, bait)
        if n >= rnd:
            return f
    return fish[ len(fish) - 1 ]

def moveTo(curX, curY, x, y, w, h, currTime):
    mfailed = { 'currentTime': currTime, 'status': 'uncool' }
    if (x < 0 or y < 0 or x >= w or y >= h):
        return mfailed
    timeNeeded = (abs(curX - x) + abs(curY - y)) * 0.2
    if (currTime + timeNeeded > 11.5):
        mfailed['reason'] = 'The day is about to end. Try moving to a closer point!'
        return mfailed
    return { 'currentTime': currTime + timeNeeded, 'status': 'ok' }
