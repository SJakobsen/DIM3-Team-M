class World
    @canvasWidth = 500
    @canvasHeight = 400

    @worldWidth = 20
    @worldHeight = 16

    @tileWidth = World.canvasWidth / World.worldWidth
    @tileHeight = World.canvasHeight / World.worldHeight

    worldArray = null

    constructor: (@canvas) ->
        @ctx = @canvas.getContext "2d"
        @canvas.width = World.canvasWidth
        @canvas.height = World.canvasHeight

        $(@canvas).click (event) =>
            @worldClicked(event)

    addLake: (lake) ->
        @worldArray = lake.getLakeArray()

   
    drawBackground: () ->
   
    drawDecorations: () ->

    drawLake: () ->
        for i in [0...World.worldWidth]
            for j in [0...World.worldHeight]
                depth = @worldArray[i][j]
                if depth > 0
                    tileColor = @getTileColorByDepth depth
                    @setTile i, j, tileColor

    drawScene: () ->
        @drawBackground()
        @drawDecorations()
        @drawLake()

    setTile: (x, y, color) ->
        coords = @getCoordsByIndex x, y
        
        @ctx.fillStyle = color
        
        @ctx.fillRect coords.x1, coords.y1, coords.x2, coords.y2

    
    getTileColorByDepth: (depth) ->
        color = 255 - (depth - 1) * 15
        code = color.toString(16)
        return "#0000"+code

    getCoordsByIndex: (x, y) ->        
        x1 = World.tileWidth * x
        y1 = World.tileHeight * y

        x2 = x1 + World.tileWidth
        y2 = y1 + World.tileHeight
        return {"x1" : x1, "y1": y1, "x2": x2, "y2": y2}
    
    getIndicesByCoords: (x, y) ->
        xx = Math.ceil(x / World.tileWidth)
        yy = Math.ceil(y / World.tileHeight)
        return {x: xx, y: yy}
        

    worldClicked: (event) ->
        x = event.offsetX
        y = event.offsetY
        indices = @getIndicesByCoords x, y
        @tileClicked indices.x, indices.y

    tileClicked: (x, y) ->
        console.log x + " " + y

    settings: (data) ->
        if data.worldWidth
            World.worldWidth = data.worldWidth
        if data.worldHeight
            World.worldHeight = data.worldHeight

    getWorldArray: () ->
        return @worldArray