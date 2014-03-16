currentX = 0;
currentY = 0;

nextX = 0;
nextY = 0;

newGame = () ->
	sendRequest {type: newgameRequest}

move = (x, y) ->
	boat = world.getBoat();
	boat.setNextX x
	boat.setNextY y

	sendRequest {type: moveRequest, data: {x: x, y: y}}	

fish = () ->
	sendRequest {type: fishRequest}

changebate = (id) ->
	sendRequest {type: changebateRequest, data: {id: id}}

buybait = (id) ->
	sendRequest {type: buybaitRequest, data: {id: id}}

buyboat = (id) ->
	sendRequest {type: buyboatRequest, data: {id: id}}

finish = () ->
	sendRequest {type: finishRequest}
