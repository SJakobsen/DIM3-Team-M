initUI = () ->
	$("#fish").click () ->
		fish()


showFishingResults = (result) ->
	res = JSON.stringify result
	$("#fishing-result").html(res);

waitUI = () ->
	
unwaitUI = () ->