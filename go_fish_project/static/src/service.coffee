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

getWeatherString = (weather, time) ->
	hour = Math.floor time
	hour = 11 if hour > 11
	weather = weather[hour]
	str = "<small>It is "

	str += switch weather.clouds
		when 0 then "sunny, "
		when 1 then "overcast, "
		else "cloudy, "

	str += switch weather.rain
		when 1 then "with a bit of rain, "
		when 2 then "with a pouring rain, "
		else ""

	str += "wind "
	str += switch weather.winddir
		when 0 then "North, "
		when 1 then "East, "
		when 2 then "South, "
		else "West, "

	str += "<strong>#{Math.round(weather.windms)}</strong>&nbsp;m/s. "

	str += "Temperature <strong>#{Math.round(weather.temp)}</strong>&nbsp;°C."

	return str + "</small>"

