// Generated by CoffeeScript 1.6.3
var Boat, Lake, World, buybait, buybaitCallback, buybaitRequest, buyboat, buyboatCallback, buyboatRequest, changebate, changebateCallback, changebateRequest, finish, finishCallback, finishRequest, fish, fishCallback, fishImages, fishRequest, getFishImage, getTimeString, initUI, lake, move, moveCallback, moveRequest, newGame, newgameCallback, newgameRequest, origin, preloadFishImages, print, sendRequest, showFishingResults, showMessage, showMoveResult, unwaitUI, updateTime, waitUI, world;

print = function(str) {
  return console.log(str);
};

getTimeString = function(time) {
  var decimal, hours, minutes, str;
  time += 6;
  hours = Math.floor(time);
  str = "";
  if (time < 10) {
    str += "0" + hours;
  } else {
    str += hours;
  }
  str += ":";
  decimal = time % 1;
  minutes = Math.floor(decimal * 60);
  if (minutes < 10) {
    str += "0" + minutes;
  } else {
    str += minutes;
  }
  return str;
};

origin = location.origin + "/gofish/api/";

newgameCallback = function(data) {
  var lake, lakeArray;
  lakeArray = data.lake;
  lake = new Lake(lakeArray);
  world.addLake(lake);
  world.addBoat(new Boat(data.x, data.y));
  world.drawScene();
  return updateTime(data.currentTime);
};

moveCallback = function(data) {
  var status;
  status = data.status;
  if (status === "ok") {
    world.boat.applyNextCoordinates();
    world.updateScene();
  }
  showMoveResult(data);
  return updateTime(data.currentTime);
};

fishCallback = function(data) {
  showFishingResults(data);
  updateTime(data.currentTime);
  if (data.end_of_game) {
    return finish();
  }
};

changebateCallback = function() {};

buybaitCallback = function() {};

buyboatCallback = function() {};

finishCallback = function(data) {
  print(data);
  return newGame();
};

newgameRequest = {
  address: "newgame/",
  callback: newgameCallback
};

moveRequest = {
  address: "move/",
  callback: moveCallback
};

fishRequest = {
  address: "fish/",
  callback: fishCallback
};

changebateRequest = {
  address: "change/bait/",
  callback: changebateCallback
};

buybaitRequest = {
  address: "buy/bate/",
  callback: buybaitCallback
};

buyboatRequest = {
  address: "buy/boat/",
  callback: buyboatCallback
};

finishRequest = {
  address: "finish/",
  callback: finishCallback
};

sendRequest = function(request) {
  var requestData;
  requestData = null;
  if (request.data) {
    requestData = request.data;
  }
  waitUI();
  $.ajax({
    type: 'POST',
    url: origin + request.type.address,
    data: requestData,
    success: function(data) {
      console.log("Success: " + request);
      request.type.callback(data);
      return unwaitUI();
    },
    error: function(err) {
      return console.log("Error: " + request);
    }
  });
  return console.log("Request sent: " + request);
};

fishImages = {
  "bream": {
    address: "/static/img/fish/bream.gif",
    img: new Image()
  },
  "catfish": {
    address: "/static/img/fish/catfish.gif",
    img: new Image()
  },
  "zander": {
    address: "/static/img/fish/zander.gif",
    img: new Image()
  },
  "whitefish": {
    address: "/static/img/fish/whitefish.gif",
    img: new Image()
  },
  "salmon": {
    address: "/static/img/fish/salmon.gif",
    img: new Image()
  },
  "perch": {
    address: "/static/img/fish/perch.gif",
    img: new Image()
  },
  "pike": {
    address: "/static/img/fish/pike.gif",
    img: new Image()
  }
};

preloadFishImages = function() {
  var key, value, _results;
  _results = [];
  for (key in fishImages) {
    value = fishImages[key];
    _results.push(value.img.src = value.address);
  }
  return _results;
};

getFishImage = function(name) {
  return fishImages[name].img;
};

Boat = (function() {
  var currentX, currentY, nextX, nextY;

  currentX = 0;

  currentY = 0;

  nextX = 0;

  nextY = 0;

  function Boat(x, y) {
    currentX = x;
    currentY = y;
  }

  Boat.prototype.getCurrentX = function() {
    return currentX;
  };

  Boat.prototype.getCurrentY = function() {
    return currentY;
  };

  Boat.prototype.setCurrentX = function(x) {
    return currentX = x;
  };

  Boat.prototype.setCurrentY = function(y) {
    return currentY = y;
  };

  Boat.prototype.getNextX = function() {
    return nextX;
  };

  Boat.prototype.getNextY = function() {
    return nextY;
  };

  Boat.prototype.setNextX = function(x) {
    return nextX = x;
  };

  Boat.prototype.setNextY = function(y) {
    return nextY = y;
  };

  Boat.prototype.applyNextCoordinates = function() {
    currentX = nextX;
    return currentY = nextY;
  };

  return Boat;

})();

Lake = (function() {
  var lakeArray;

  lakeArray = [];

  function Lake(lake) {
    lakeArray = lake;
  }

  Lake.prototype.getLakeArray = function() {
    return lakeArray;
  };

  return Lake;

})();

World = (function() {
  var boat, worldArray;

  World.canvasWidth = 500;

  World.canvasHeight = 400;

  World.worldWidth = 20;

  World.worldHeight = 16;

  World.tileWidth = World.canvasWidth / World.worldWidth;

  World.tileHeight = World.canvasHeight / World.worldHeight;

  World.bgcolors = ['error', '#64ccfc', '#1eaad8', '#1c91ff', '#1c67ff', '#0032ff', '#0000ff', '#0000bb', '#000088', '#000044', '#000022'];

  worldArray = null;

  boat = null;

  function World(canvas) {
    var _this = this;
    this.canvas = canvas;
    this.ctx = this.canvas.getContext("2d");
    this.canvas.width = World.canvasWidth;
    this.canvas.height = World.canvasHeight;
    $(this.canvas).click(function(event) {
      return _this.worldClicked(event);
    });
  }

  World.prototype.addLake = function(lake) {
    return this.worldArray = lake.getLakeArray();
  };

  World.prototype.addBoat = function(boat) {
    return this.boat = boat;
  };

  World.prototype.drawBackground = function() {};

  World.prototype.drawDecorations = function() {};

  World.prototype.drawLake = function() {
    var depth, i, j, tileColor, _i, _ref, _results;
    _results = [];
    for (i = _i = 0, _ref = World.worldHeight; 0 <= _ref ? _i < _ref : _i > _ref; i = 0 <= _ref ? ++_i : --_i) {
      _results.push((function() {
        var _j, _ref1, _results1;
        _results1 = [];
        for (j = _j = 0, _ref1 = World.worldWidth; 0 <= _ref1 ? _j < _ref1 : _j > _ref1; j = 0 <= _ref1 ? ++_j : --_j) {
          depth = this.worldArray[i][j];
          if (depth > 0) {
            tileColor = this.getTileColorByDepth(depth);
            _results1.push(this.setTile(j, i, tileColor));
          } else {
            _results1.push(void 0);
          }
        }
        return _results1;
      }).call(this));
    }
    return _results;
  };

  World.prototype.drawBoat = function() {
    if (this.boat) {
      return this.setTile(this.boat.getCurrentX(), this.boat.getCurrentY(), "#ff0000");
    }
  };

  World.prototype.drawScene = function() {
    this.drawBackground();
    this.drawDecorations();
    this.drawLake();
    return this.drawBoat();
  };

  World.prototype.updateScene = function() {
    return this.drawScene();
  };

  World.prototype.setTile = function(x, y, color) {
    var coords;
    coords = this.getCoordsByIndex(x, y);
    this.ctx.fillStyle = color;
    return this.ctx.fillRect(coords.x, coords.y, World.tileWidth, World.tileHeight);
  };

  World.prototype.getTileColorByDepth = function(depth) {
    return World.bgcolors[depth];
  };

  World.prototype.getCoordsByIndex = function(x, y) {
    var x1, y1;
    x1 = World.tileWidth * x;
    y1 = World.tileHeight * y;
    return {
      "x": x1,
      "y": y1
    };
  };

  World.prototype.getIndicesByCoords = function(x, y) {
    var xx, yy;
    xx = Math.floor(x / World.tileWidth);
    yy = Math.floor(y / World.tileHeight);
    return {
      x: xx,
      y: yy
    };
  };

  World.prototype.worldClicked = function(event) {
    var indices, x, y;
    x = event.offsetX;
    y = event.offsetY;
    indices = this.getIndicesByCoords(x, y);
    return this.tileClicked(indices.x, indices.y);
  };

  World.prototype.tileClicked = function(x, y) {
    return move(x, y);
  };

  World.prototype.settings = function(data) {
    if (data.worldWidth) {
      World.worldWidth = data.worldWidth;
    }
    if (data.worldHeight) {
      return World.worldHeight = data.worldHeight;
    }
  };

  World.prototype.getWorldArray = function() {
    return this.worldArray;
  };

  World.prototype.getBoat = function() {
    return this.boat;
  };

  return World;

})();

initUI = function() {
  return $("#fish").click(function() {
    return fish();
  });
};

showFishingResults = function(result) {
  var res, x, _i, _len, _ref;
  res = JSON.stringify(result);
  if (result.fish.length > 0) {
    if (result.fish.length > 1) {
      res = "Yay! You have caught some fishes! Take a look at them!";
    } else {
      res = "Yay! You have caught a fish! Take a look at it!";
    }
    res += "<ul>";
    _ref = result.fish;
    for (_i = 0, _len = _ref.length; _i < _len; _i++) {
      x = _ref[_i];
      res += "<li>" + x.fish + " has price " + x.price + ", weight: " + x.weight + " and size: " + x.size + "</li>";
    }
    res += "</ul>";
  } else {
    res = "Sorry, no fish was caught :(";
  }
  return showMessage(res);
};

showMoveResult = function(result) {
  if (result.status === "ok") {
    return showMessage("You have successfully moved!");
  } else {
    return showMessage("You can not move. Reason: " + result.reason);
  }
};

showMessage = function(msg) {
  $("#message").hide();
  $("#message").html(msg);
  return $("#message").slideDown("fast");
};

updateTime = function(time) {
  return $("#time").html(getTimeString(time));
};

waitUI = function() {};

unwaitUI = function() {};

newGame = function() {
  return sendRequest({
    type: newgameRequest
  });
};

move = function(x, y) {
  var boat;
  boat = world.getBoat();
  boat.setNextX(x);
  boat.setNextY(y);
  return sendRequest({
    type: moveRequest,
    data: {
      x: x,
      y: y
    }
  });
};

fish = function() {
  return sendRequest({
    type: fishRequest
  });
};

changebate = function(id) {
  return sendRequest({
    type: changebateRequest,
    data: {
      id: id
    }
  });
};

buybait = function(id) {
  return sendRequest({
    type: buybaitRequest,
    data: {
      id: id
    }
  });
};

buyboat = function(id) {
  return sendRequest({
    type: buyboatRequest,
    data: {
      id: id
    }
  });
};

finish = function() {
  return sendRequest({
    type: finishRequest
  });
};

world = null;

lake = null;

$(document).ready(function() {
  world = new World($("#world")[0]);
  initUI();
  preloadFishImages();
  return newGame();
});
