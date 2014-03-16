class Lake
	lakeArray = []

	constructor: (lake) ->
		if lake.lakeArray
			lakeArray = lake.lakeArray

	getLakeArray: () ->
		return lakeArray