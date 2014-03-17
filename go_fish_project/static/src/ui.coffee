initUI = () ->
	$("#fish").click () ->
		fish()

	$("#new-game").click () ->
		newGame()


showFishingResults = (result) ->
	res = JSON.stringify result
	
	if result.fish.length > 0
		if result.fish.length > 1
			res = "<p>Yay! You have caught some fishes! Take a look at them!</p>"

		else 
			res = "<p>Yay! You have caught a fish! Take a look at it!</p>"

		res += "<ul class='row'>"
		for x in result.fish
			res += """
				<li class='span4'>
					#{getFishImage(x.fish).outerHTML}
					<small><strong>#{x.fish}:</strong> #{x.weight}&nbsp;kg, #{x.size}&nbsp;cm. +#{x.price}&nbsp;monies</small>
				</li>
			"""
		res += "</ul>"
	else
		res = "<p>Sorry, no fish was caught :(</p>"

	if result.fish.length > 0
		str = ""
		for x in result.fish
			str += "<li class='new'>#{getFishImage(x.fish).outerHTML}"
			str += "#{x.fish}: #{x.weight}&nbsp;kg, +#{x.price}&nbsp;monies"
			str += "</li>"

		$(".new").removeClass("new");
		$("#current-catches ul").prepend(str)



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

updateWeather = (weather, time) ->
	$('#weather').html getWeatherString(weather, time)

updateMoney = (money) ->
	$('#money').html money

showGameResults = (data) ->
	el = $("#game-result")
	str = ""
	str += "<h2>The day is over!</h2><div> You have earned #{data.money} monies!</div>"
	if data.trophies.length > 0
		str += "<div> Your trophies are: "
		str += "<ul class='row'>"
		for x in data.trophies
			str += "<li class='span4'>#{getFishImage(x.name).outerHTML}<small><strong>#{x.name}:</strong> #{x.weight}&nbsp;kg, #{x.size}&nbsp;cm. +#{x.price}&nbsp;monies</small></li>"
		str += '</ul>'
	$("#info", el).html(str);
	el.show()
	$('body').animate({
		scrollTop: el.offset().top
	}, 500);

hideGameResults = () ->
	$("#game-result").hide()
	$('body').animate({
		scrollTop: 0
	}, 500);	



waitUI = () ->
	
unwaitUI = () ->
