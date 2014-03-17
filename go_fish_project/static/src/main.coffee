world = null
lake = null



$(document).ready () ->
	world = new World $("#world")[0]

	# get settings
	# world.settings({})

	initUI()
	
	preloadFishImages()

	newGame()