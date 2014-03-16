world = null



$(document).ready () ->
	world = new World $("#world")[0]

	# get settings

	# world.settings({})

	newGame();

	lake = generateLakeData()
	lake = new Lake(lake)

	world.addLake(lake)
	world.drawScene()





generateLakeData = () ->
	lake = new Array World.worldWidth
	for i in [0...World.worldWidth]
		lake[i] = new Array World.worldHeight
	
	for i in [0...World.worldWidth]
		for j in [0...World.worldHeight]
			lake[i][j] = Math.floor(Math.random() * 10 + 1)		
	return {lakeArray: lake}

