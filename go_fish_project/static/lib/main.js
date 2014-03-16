// Generated by CoffeeScript 1.6.3
var Lake, World, buybait, buybaitCallback, buybaitRequest, buyboat, buyboatCallback, buyboatRequest, changebate, changebateCallback, changebateRequest, finish, finishCallback, finishRequest, fish, fishCallback, fishRequest, generateLakeData, move, moveCallback, moveRequest, newGame, newgameCallback, newgameRequest, origin, sendRequest, unwaitUI, waitUI, world;

origin = "";

newgameCallback = function() {};

moveCallback = function() {};

fishCallback = function() {};

changebateCallback = function() {};

buybaitCallback = function() {};

buyboatCallback = function() {};

finishCallback = function() {};

newgameRequest = {
  address: "newgame",
  callback: newgameCallback
};

moveRequest = {
  address: "move",
  callback: moveCallback
};

fishRequest = {
  address: "fish",
  callback: fishCallback
};

changebateRequest = {
  address: "change/bait",
  callback: changebateCallback
};

buybaitRequest = {
  address: "buy/bate",
  callback: buybaitCallback
};

buyboatRequest = {
  address: "buy/boat",
  callback: buyboatCallback
};

finishRequest = {
  address: "finish",
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
    type: 'GET',
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

Lake = (function() {
  var lakeArray;

  lakeArray = [];

  function Lake(lake) {
    if (lake.lakeArray) {
      lakeArray = lake.lakeArray;
    }
  }

  Lake.prototype.getLakeArray = function() {
    return lakeArray;
  };

  return Lake;

})();

World = (function() {
  var worldArray;

  World.canvasWidth = 500;

  World.canvasHeight = 400;

  World.worldWidth = 20;

  World.worldHeight = 16;

  World.tileWidth = World.canvasWidth / World.worldWidth;

  World.tileHeight = World.canvasHeight / World.worldHeight;

  worldArray = null;

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

  World.prototype.drawBackground = function() {};

  World.prototype.drawDecorations = function() {};

  World.prototype.drawLake = function() {
    var depth, i, j, tileColor, _i, _ref, _results;
    _results = [];
    for (i = _i = 0, _ref = World.worldWidth; 0 <= _ref ? _i < _ref : _i > _ref; i = 0 <= _ref ? ++_i : --_i) {
      _results.push((function() {
        var _j, _ref1, _results1;
        _results1 = [];
        for (j = _j = 0, _ref1 = World.worldHeight; 0 <= _ref1 ? _j < _ref1 : _j > _ref1; j = 0 <= _ref1 ? ++_j : --_j) {
          depth = this.worldArray[i][j];
          if (depth > 0) {
            tileColor = this.getTileColorByDepth(depth);
            _results1.push(this.setTile(i, j, tileColor));
          } else {
            _results1.push(void 0);
          }
        }
        return _results1;
      }).call(this));
    }
    return _results;
  };

  World.prototype.drawScene = function() {
    this.drawBackground();
    this.drawDecorations();
    return this.drawLake();
  };

  World.prototype.setTile = function(x, y, color) {
    var coords;
    coords = this.getCoordsByIndex(x, y);
    this.ctx.fillStyle = color;
    return this.ctx.fillRect(coords.x1, coords.y1, coords.x2, coords.y2);
  };

  World.prototype.getTileColorByDepth = function(depth) {
    var code, color;
    color = 255 - (depth - 1) * 15;
    code = color.toString(16);
    return "#0000" + code;
  };

  World.prototype.getCoordsByIndex = function(x, y) {
    var x1, x2, y1, y2;
    x1 = World.tileWidth * x;
    y1 = World.tileHeight * y;
    x2 = x1 + World.tileWidth;
    y2 = y1 + World.tileHeight;
    return {
      "x1": x1,
      "y1": y1,
      "x2": x2,
      "y2": y2
    };
  };

  World.prototype.getIndicesByCoords = function(x, y) {
    var xx, yy;
    xx = Math.ceil(x / World.tileWidth);
    yy = Math.ceil(y / World.tileHeight);
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
    return console.log(x + " " + y);
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

  return World;

})();

waitUI = function() {};

unwaitUI = function() {};

newGame = function() {
  return sendRequest({
    type: newgameRequest
  });
};

move = function(x, y) {
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

$(document).ready(function() {
  var lake;
  world = new World($("#world")[0]);
  newGame();
  lake = generateLakeData();
  lake = new Lake(lake);
  world.addLake(lake);
  return world.drawScene();
});

generateLakeData = function() {
  var i, j, lake, _i, _j, _k, _ref, _ref1, _ref2;
  lake = new Array(World.worldWidth);
  for (i = _i = 0, _ref = World.worldWidth; 0 <= _ref ? _i < _ref : _i > _ref; i = 0 <= _ref ? ++_i : --_i) {
    lake[i] = new Array(World.worldHeight);
  }
  for (i = _j = 0, _ref1 = World.worldWidth; 0 <= _ref1 ? _j < _ref1 : _j > _ref1; i = 0 <= _ref1 ? ++_j : --_j) {
    for (j = _k = 0, _ref2 = World.worldHeight; 0 <= _ref2 ? _k < _ref2 : _k > _ref2; j = 0 <= _ref2 ? ++_k : --_k) {
      lake[i][j] = Math.floor(Math.random() * 10 + 1);
    }
  }
  return {
    lakeArray: lake
  };
};
