print = (str) ->
	console.log str

getTimeString = (time) ->
	time += 6;
	hours = Math.floor time
	str = ""
	if time < 10
		str += "0" + hours
	else
		str += hours

	str += ":"

	decimal = time % 1

	minutes = Math.floor(decimal * 60);
	if minutes < 10
		str += "0" + minutes
	else
		str += minutes

	return str
