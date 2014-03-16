from random import randint
from math import floor

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