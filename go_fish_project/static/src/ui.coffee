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

		res += "<ul>"
		for x in result.fish
			res += "<li>"+x.fish+" has price "+x.price+", weight: "+x.weight+" and size: "+x.size+"</li>"
		res += "</ul>"
	else
		res = "Sorry, no was fish caught :("

	$("#fishing-result").html(res);

waitUI = () ->
	
unwaitUI = () ->