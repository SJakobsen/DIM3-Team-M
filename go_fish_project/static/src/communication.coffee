origin = "http://127.0.0.1:8000/gofish/api/"


newgameCallback = (data) ->
	lakeArray = data.lake
	lake = new Lake lakeArray
	world.addLake(lake)
	world.addBoat(new Boat())
	world.drawScene()

	updateTime data.currentTime

moveCallback = (data) ->
	status = data.status
	if status == "ok"
		world.boat.applyNextCoordinates()
		world.updateScene()
	showMoveResult(data)

	updateTime data.currentTime

fishCallback = (data) ->
	showFishingResults data
	updateTime data.currentTime
	
changebateCallback = () ->
buybaitCallback = () ->
buyboatCallback = () ->
finishCallback = () ->

newgameRequest  = {address: "newgame/", callback: newgameCallback};
moveRequest = {address: "move/", callback: moveCallback}
fishRequest = {address: "fish/", callback: fishCallback}
changebateRequest = {address: "change/bait/", callback: changebateCallback}
buybaitRequest = {address: "buy/bate/", callback: buybaitCallback}
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