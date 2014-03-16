import os

def populate():
    #populate_fish---------------------------------------------------------
    #reference from http://fogu.com/hm/animal_parade/fishing.php
    #size 20 = trophysize 10 = large, 5 = medium, 1 = small
    
    fish = {
        'salmon': {
            'name': 'salmon', 'base_price': 200, 'base_chance': 5,
            'size_mean': 100, 'size_sd': 20,
            'weight_mean': 15, 'weight_sd': 3,
            'p_depth': 0, 'p_bsize': 1,
            'p_clouds': 1, 'p_rain': 1, 'p_wind': 1
        },
        'pike': {
            'name': 'pike', 'base_price': 50, 'base_chance': 50,
            'size_mean': 100, 'size_sd': 20,
            'weight_mean': 5, 'weight_sd': 2,
            'p_depth': 1, 'p_bsize': 2,
            'p_clouds': 1, 'p_rain': 1, 'p_wind': 1
        },
        'perch': {
            'name': 'perch', 'base_price': 10, 'base_chance': 75,
            'size_mean': 25, 'size_sd': 5,
            'weight_mean': 0.7, 'weight_sd': 0.3,
            'p_depth': 0, 'p_bsize': 0,
            'p_clouds': 0, 'p_rain': 0, 'p_wind': 1
        },
        'zander': {
            'name': 'zander', 'base_price': 50, 'base_chance': 50,
            'size_mean': 60, 'size_sd': 15,
            'weight_mean': 3, 'weight_sd': 1,
            'p_depth': 2, 'p_bsize': 2,
            'p_clouds': 2, 'p_rain': 2, 'p_wind': 2
        },
        'catfish': {
            'name': 'catfish', 'base_price': 300, 'base_chance': 10,
            'size_mean': 140, 'size_sd': 40,
            'weight_mean': 16, 'weight_sd': 8,
            'p_depth': 3, 'p_bsize': 3,
            'p_clouds': 2, 'p_rain': 1, 'p_wind': 1
        },
        'bream': {
            'name': 'bream', 'base_price': 35, 'base_chance': 40,
            'size_mean': 40, 'size_sd': 10,
            'weight_mean': 3, 'weight_sd': 1,
            'p_depth': 2, 'p_bsize': 0,
            'p_clouds': 1, 'p_rain': 0, 'p_wind': 1
        },
        'whitefish': {
            'name': 'whitefish', 'base_price': 60, 'base_chance': 30,
            'size_mean': 30, 'size_sd': 10,
            'weight_mean': 1, 'weight_sd': 0.3,
            'p_depth': 2, 'p_bsize': 0,
            'p_clouds': 1, 'p_rain': 1, 'p_wind': 0
        }
    }

    for f in fish:
        add_fish(fish[f])

    #populate_boat-----------------------------------------------------------
    add_boat('wooden_boat',10, 20)
    add_boat('jon_boat',15, 100)
    add_boat('bay_fishing_boat',20,200)
    add_boat('flats_boat',30,1000)
    add_boat('offshore_fishing_boat',40,2000)
    add_boat('center_console_boat',50,4000)
    add_boat('walkaround_boat',60,4500)
    add_boat('fish_and_ski_boat',90,6000)
    add_boat('big_boat',150,10000)
    add_boat('kiel_nc_105',300,20000)
    
    #populate_player---------------------------------------------------------
#    a = add_player(0,100)
#    b = add_player(0,100)
#    c = add_player(0,100)
#    d = add_player(0,100)
#    e = add_player(0,100)

    #populate_game---------------------------------------------------------
#    add_game('pond','sunny',a)
#    add_game('island','cloudy',b)
#    add_game('waterfall','hurricane',c)
#    add_game('river','thunderstorm',d)
#    add_game('ocean','snow',e)

    #populate_bait---------------------------------------------------------
    baits = {
        'Small white rotex spinner': {
            'name': 'Small_white_rotex_spinner', 'colour': 0, 'size': 0, 'price': 2000
        },
        'Small red rotex spinner': {
            'name': 'Small_red_rotex_spinner', 'colour': 1, 'size': 0, 'price': 2000
        },
        'Medium white rotex spinner': {
            'name': 'Medium_white_rotex_spinner', 'colour': 0, 'size': 1, 'price': 2500
        },
        'Medium yellow rotex spinner': {
            'name': 'Medium_yellow_rotex_spinner', 'colour': 1, 'size': 0, 'price': 2500
        },
        'Silver spoon': {
            'name': 'Silver_spoon', 'colour': 0, 'size': 2, 'price': 1500
        },
        'Bronze spoon': {
            'name': 'Bronze_spoon', 'colour': 1, 'size': 2, 'price': 1500
        },
        'Redhead wobbler': {
            'name': 'Redhead_wobbler', 'colour': 0, 'size': 2, 'price': 3000
        },
        'Tiger wobbler': {
            'name': 'Tiger_wobbler', 'colour': 1, 'size': 2, 'price': 3000
        },
        'Massive green wobbler': {
            'name': 'Massive_green_wobbler', 'colour': 0, 'size': 3, 'price': 10000
        },
        'Blue lure': {
            'name': 'Blue_lure', 'colour': 0, 'size': 2, 'price': 1000
        },
        'Yellow lure': {
            'name': 'Yellow_lure', 'colour': 1, 'size': 2, 'price': 1000
        },
        'Small red lure': {
            'name': 'Small_red_lure', 'colour': 1, 'size': 0, 'price': 500
        },
        'Small green lure': {
            'name': 'Small_green_lure', 'colour': 0, 'size': 0, 'price': 500
        }
    }

    for b in baits:
        add_bait(baits[b])

    #show all the fish**********
    print "----------------------------------------"
    print "These are all fish in the game: "
    fishcount = 0
    for f in Fish.objects.all():
        fishcount +=1
        print str(fishcount)+". "+str(f)
    print "Total number of fish is: "+str(fishcount)

    #show all the boat**********
    print "----------------------------------------"
    print "These are all boats in the game: "
    boatcount = 0
    for b in Boat.objects.all():
        boatcount +=1
        print str(boatcount)+". "+str(b)
    print "Total number of boat is: "+str(boatcount)

    #show all the bait**********
    print "----------------------------------------"
    print "These are all baits in the game: "
    baitcount = 0
    for b in Bait.objects.all():
        baitcount +=1
        print str(baitcount)+". "+str(b)
    print "Total number of bait is: "+str(baitcount)

    #show all the player**********
    print "----------------------------------------"
    print "These are all players in the game: "
    playercount = 0
    for p in Player.objects.all():
            playercount +=1
            print str(playercount)+". "+str(p)
    print "Total number of player is: "+str(playercount)

    #show all the trophy**********
    print "----------------------------------------"
    print "These are all trophys in the game: "
    trophycount = 0
    for t in Trophy.objects.all():
        trophycount +=1
        print str(trophycount)+". "+str(t)
    print "Total number of trophy is: "+str(trophycount)

    #show all the currently games**********
    print "----------------------------------------"
    print "These are all games in process: "
    gamecount = 0
    for g in Game.objects.all():
        gamecount +=1
        print str(gamecount)+". "+str(g)
    print "Total number of game is: "+str(gamecount)


def add_fish(fh):
    f = Fish.objects.get_or_create(
        name=fh['name'],
        base_price=fh['base_price'],
        base_chance=fh['base_chance'],
        size_mean=fh['size_mean'],
        size_sd=fh['size_sd'],
        weight_mean=fh['weight_mean'],
        weight_sd=fh['weight_sd'],
        p_depth=fh['p_depth'],
        p_bsize=fh['p_bsize'],
        p_clouds=fh['p_clouds'],
        p_rain=fh['p_rain'],
        p_wind=fh['p_wind']
    )[0]
    return f

def add_game(lakein,weatherin,playerin):
    g = Game.objects.get_or_create(lake=lakein,weather=weatherin,player=playerin)
    return g

def add_caughtfish(fishin,gamein,amountin):
    cf = CaughtFish.objects.get_or_create(fish=fishin,game=gamein,amount=amountin)
    return cf

def add_bait(h):
    b = Bait.objects.get_or_create(
        name=h['name'],
        colour=h['colour'],
        size=h['size'],
        price=h['price']
    )[0]
    return b

def add_boat(namein,speedin,pricein):
    b = Boat.objects.get_or_create(name=namein,speed=speedin,price=pricein)[0]
    return b


def add_player(rankingin,moneyin):
    p = Player.objects.get_or_create(ranking=rankingin,money=moneyin)[0]
    return p

def add_trophy(namein,fishin,playerin=None):
    t = Trophy.objects.get_or_create(name=namein,fish=fishin,player=playerin)
    return t

def add_ownsbait(playerin,baitin,amountin):
    cb = OwnsBait.objects.get_or_create(player=playerin,bait=baitin,amount=amountin)
    return cb


if __name__ == '__main__':
    print "Starting Gofish population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','go_fish_project.settings')
    from gofish.models import Fish, Game, CaughtFish, Bait, Boat, Player, Trophy, OwnsBait
    populate()
