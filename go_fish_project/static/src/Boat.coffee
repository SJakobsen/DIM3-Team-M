class Boat
    currentX = 0;
    currentY = 0;

    nextX = 0;
    nextY = 0;

    boatImage = new Image();
    boatImage.onload = () ->
        world.drawBoat()

    constructor: (x, y) ->
        boatImage.src = "/static/img/boats/boat.gif"

        currentX = x
        currentY = y

    getCurrentX: () ->
        return currentX

    getCurrentY: () ->
        return currentY

    setCurrentX: (x) ->
        currentX = x

    setCurrentY: (y) ->
        currentY = y

    getNextX: () ->
        return nextX

    getNextY: () ->
        return nextY

    setNextX: (x) ->
        nextX = x

    setNextY: (y) ->
        nextY = y

    applyNextCoordinates: () ->
        currentX = nextX
        currentY = nextY

    getBoatImage: () ->
        return boatImage