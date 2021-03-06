origin = location.origin + "/gofish/api/"


newgameCallback = (data) ->
	$("#message").empty()
	hideGameResults()
	$("#current-catches ul").empty()

	lakeArray = data.lake
	lake = new Lake lakeArray
	world.setWeather(data.weather)
	world.addLake(lake)
	world.addBoat(new Boat(data.x, data.y))
	world.drawScene()

	updateTime data.currentTime
	updateWeather world.getWeather(), data.currentTime
	updateMoney data.money

moveCallback = (data) ->
	status = data.status
	if status == "ok"
		world.boat.applyNextCoordinates()
		world.updateScene()
	showMoveResult(data)

	updateTime data.currentTime
	updateWeather world.getWeather(), data.currentTime

fishCallback = (data) ->
	showFishingResults data
	updateTime data.currentTime
	updateWeather world.getWeather(), data.currentTime
	if data.end_of_game
		finish()

	
changebaitCallback = () ->
buybaitCallback = () ->
buyboatCallback = () ->
finishCallback = (data) ->
	showGameResults data

newgameRequest  = {address: "newgame/", callback: newgameCallback};
moveRequest = {address: "move/", callback: moveCallback}
fishRequest = {address: "fish/", callback: fishCallback}
changebaitRequest = {address: "change/bait/", callback: changebaitCallback}
buybaitRequest = {address: "buy/bait/", callback: buybaitCallback}
buyboatRequest = {address: "buy/boat/", callback: buyboatCallback}
finishRequest = {address: "finish/", callback: finishCallback}

sendRequest = (request) ->
	requestData = null
	if request.data
		requestData = request.data

	waitUI();

	$.ajax {
		type: 'POST',
		url: origin+request.type.address,
		data: requestData,
		success: (data) ->
			console.log "Success: " + request
			request.type.callback(data)
			unwaitUI();
		,
		error: (err) ->
			console.log "Error: " + request
			# errorCallback err
	}
	console.log "Request sent: " + request
