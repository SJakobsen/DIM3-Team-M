class World
    @canvasWidth = 500
    @canvasHeight = 400

    @worldWidth = 20
    @worldHeight = 16

    @tileWidth = World.canvasWidth / World.worldWidth
    @tileHeight = World.canvasHeight / World.worldHeight

    worldArray = null

    boat = null

    constructor: (@canvas) ->
        @ctx = @canvas.getContext "2d"
        @canvas.width = World.canvasWidth
        @canvas.height = World.canvasHeight

        $(@canvas).click (event) =>
            @worldClicked(event)

    addLake: (lake) ->
        @worldArray = lake.getLakeArray()

    addBoat: (boat) ->
        @boat = boat

   
    drawBackground: () ->
   
    drawDecorations: () ->

    drawLake: () ->
        for i in [0...World.worldHeight]
            for j in [0...World.worldWidth]
                depth = @worldArray[i][j]
                if depth > 0
                    tileColor = @getTileColorByDepth depth
                    @setTile i, j, tileColor
    drawBoat: () ->
        if @boat
            @setTile @boat.getCurrentX(), @boat.getCurrentY(), "#ff0000"

    drawScene: () ->
        @drawBackground()
        @drawDecorations()
        @drawLake()
        @drawBoat()

    updateScene: () ->
        @drawScene()

    setTile: (x, y, color) ->
        coords = @getCoordsByIndex x, y
        @ctx.fillStyle = color
        @ctx.fillRect coords.x, coords.y, World.tileWidth, World.tileHeight

    
    getTileColorByDepth: (depth) ->
        color = 255 - (depth - 1) * 15
        code = color.toString(16)
        return "#0000"+code

    getCoordsByIndex: (x, y) ->       
        x1 = World.tileWidth * x
        y1 = World.tileHeight * y

        # x2 = x1 + World.tileWidth
        # y2 = y1 + World.tileHeight
        return {"x" : x1, "y": y1}
    
    getIndicesByCoords: (x, y) ->
        xx = Math.floor(x / World.tileWidth)
        yy = Math.floor(y / World.tileHeight)
        return {x: xx, y: yy}
        

    worldClicked: (event) ->
        x = event.offsetX
        y = event.offsetY
        indices = @getIndicesByCoords x, y
        @tileClicked indices.x, indices.y

    tileClicked: (x, y) ->
        move(x, y)

    settings: (data) ->
        if data.worldWidth
            World.worldWidth = data.worldWidth
        if data.worldHeight
            World.worldHeight = data.worldHeight

    getWorldArray: () ->
        return @worldArray

    getBoat: () ->
        return @boat