initUI = () ->
	$("#fish").click () ->
		fish()


showFishingResults = (result) ->
	res = JSON.stringify result
	
	if result.fish.length > 0
		if result.fish.length > 1
			res = "Yay! You have caught some fishes! Take a look at them!"

		else 
			res = "Yay! You have caught a fish! Take a look at it!"

		res += "<ul class='row'>"
		for x in result.fish
			res += "<li class='span4'><img src='' alt='#{x.fish}'/> #{x.price} monies, #{x.weight} kg, #{x.size} cm</li>"
		res += "</ul>"
	else
		res = "Sorry, no fish was caught :("

	showMessage res

showMoveResult = (result) ->
	if result.status == "ok"
		showMessage "You have successfully moved!"
	else
		showMessage "You can not move. Reason: " + result.reason

showMessage = (msg)	->
	$("#message").hide()
	$("#message").html(msg)
	$("#message").slideDown("fast")

updateTime = (time)	->
	$("#time").html getTimeString time

waitUI = () ->
	
unwaitUI = () ->
