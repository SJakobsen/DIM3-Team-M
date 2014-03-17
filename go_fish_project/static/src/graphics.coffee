fishImages = {
	"bream": {address: "/static/img/fish/bream.gif", img: new Image()} ,
	"catfish": {address: "/static/img/fish/catfish.gif", img: new Image()} ,
	"zander": {address: "/static/img/fish/zander.gif", img: new Image()} ,
	"whitefish": {address: "/static/img/fish/whitefish.gif", img: new Image()} ,
	"salmon": {address: "/static/img/fish/salmon.gif", img: new Image()} ,
	"perch": {address: "/static/img/fish/perch.gif", img: new Image()} ,
	"pike": {address: "/static/img/fish/pike.gif", img: new Image()} ,
}

preloadFishImages = () ->
	for key, value of fishImages
		value.img.src = value.address

getFishImage = (name) ->
	return fishImages[name].img