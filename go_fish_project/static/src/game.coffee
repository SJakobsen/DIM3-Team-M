newGame = () ->
	sendRequest {type: newgameRequest}

move = (x, y) ->
	boat = world.getBoat();
	boat.setNextX x
	boat.setNextY y

	sendRequest {type: moveRequest, data: {x: x, y: y}}	

fish = () ->
	sendRequest {type: fishRequest}

changebait = (id) ->
	sendRequest {type: changebaitRequest, data: {id: id}}

buybait = (id) ->
	sendRequest {type: buybaitRequest, data: {id: id}}

buyboat = (id) ->
	sendRequest {type: buyboatRequest, data: {id: id}}

finish = () ->
	sendRequest {type: finishRequest}
