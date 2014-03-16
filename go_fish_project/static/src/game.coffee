newGame = () ->
	sendRequest {type: newgameRequest}

move = (x, y) ->
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
