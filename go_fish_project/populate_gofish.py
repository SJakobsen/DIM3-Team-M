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
    
    wooden_boat = add_boat('wooden_boat',10, 20)
    jon_boat = add_boat('jon_boat',15, 100)
    bay_fishing_boat = add_boat('bay_fishing_boat',20,200)
    flats_boat = add_boat('flats_boat',30,1000)
    offshore_fishing_boat = add_boat('offshore_fishing_boat',40,2000)
    center_console_boat = add_boat('center_console_boat',50,4000)
    walkaround_boat = add_boat('walkaround_boat',60,4500)
    fish_and_ski_boat = add_boat('fish_and_ski_boat',90,6000)
    big_boat = add_boat('big_boat',150,10000)
    kiel_nc_105 = add_boat('kiel_nc_105',300,20000)
    
    #populate_bait-----------------------------------------------------------
    
    Small_white_rotex_spinner = add_bait( 'Small_white_rotex_spinner', 0, 0, 2000 )
    Small_red_rotex_spinner = add_bait( 'Small_red_rotex_spinner', 1, 0, 2000 )
    Medium_white_rotex_spinner = add_bait( 'Medium_white_rotex_spinner', 0, 1, 2500 )
    Medium_yellow_rotex_spinner = add_bait( 'Medium_yellow_rotex_spinner',1,0,2500 )
    Silver_spoon = add_bait('Silver_spoon', 0, 2, 1500 )
    Bronze_spoon = add_bait( 'Bronze_spoon', 1, 2, 1500 )
    Redhead_wobbler = add_bait( 'Redhead_wobbler', 0, 2, 3000 )
    Tiger_wobbler = add_bait( 'Tiger_wobbler',  1, 2, 3000 )
    Massive_green_wobbler = add_bait( 'Massive_green_wobbler', 0, 3, 10000 )
    Blue_lure = add_bait( 'Blue_lure', 0, 2, 1000 )
    Yellow_lure = add_bait( 'Yellow_lure', 1, 2, 1000 )
    Small_red_lure = add_bait( 'Small_red_lure', 1, 0, 500 )
    Small_green_lure = add_bait( 'Small_green_lure', 0, 0, 500 )
    
    #populate_user-----------------------------------------------------------
    
    u1 = add_user("Adam", "Adam")
    u2 = add_user("Mary", "Mary")
    u3 = add_user("Jake", "Jake")
    u4 = add_user("Penelope", "Penelope")
    u5 = add_user("Conrade", "Conrade")
    
    #populate_player---------------------------------------------------------
    
    p1 = add_player(u1, 250, wooden_boat, Small_green_lure)
    p2 = add_player(u2, 3750, offshore_fishing_boat, Small_red_rotex_spinner)
    p3 = add_player(u3, 25000, center_console_boat, Yellow_lure)
    p4 = add_player(u4, 750, bay_fishing_boat, Tiger_wobbler)
    p5 = add_player(u5, 32890, fish_and_ski_boat, Silver_spoon)
    
    #give_players_bait------------------------------------------------------
    
    add_ownsbait(p1, Small_green_lure, 1)
    add_ownsbait(p2, Small_red_rotex_spinner, 1)
    add_ownsbait(p2, Massive_green_wobbler, 2)
    add_ownsbait(p3, Yellow_lure, 3)
    add_ownsbait(p3, Bronze_spoon, 5)
    add_ownsbait(p3, Tiger_wobbler, 2)
    add_ownsbait(p4, Tiger_wobbler, 1)
    add_ownsbait(p5, Silver_spoon, 5)
    add_ownsbait(p5, Bronze_spoon, 5)

    #populate_game----------------------------------------------------------
    
#    add_game('pond','sunny',a)
#    add_game('island','cloudy',b)
#    add_game('waterfall','hurricane',c)
#    add_game('river','thunderstorm',d)
#    add_game('ocean','snow',e)


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
    
def add_user(username, password):
    u = User.objects.get_or_create(username=username, password=password)[0]
    return u

def add_game(lakein, weatherin, playerin, timein, xin, yin, attemptin):
    g = Game.objects.get_or_create(lake=lakein,weather=weatherin,  player=playerin, time=timein, x=xin, y=yin, attempt=attemptin)[0]
    return g

def add_caughtfish(fishin, gamein, sizein, weightin, pricein):
    cf = CaughtFish.objects.get_or_create(fish=fishin, game=gamein, size=sizein, weight=weightin, price=pricein)[0]
    return cf

def add_bait(namein, colourin, sizein, pricein):
    b = Bait.objects.get_or_create(name=namein, colour=colourin, size=sizein, price=pricein)[0]
    return b

def add_boat(namein,speedin,pricein):
    b = Boat.objects.get_or_create(name=namein,speed=speedin,price=pricein)[0]
    return b

def add_player(userin, moneyin, boatin, baitin):
    p = Player.objects.get_or_create(user=userin, money=moneyin, boat=boatin, bait=baitin)[0]
    return p

def add_trophy(fishin, sizein, weightin, pricein, playerin):
    t = Trophy.objects.get_or_create(fish=fishin, size=sizein, weight=weightin, price=pricein, player=playerin)[0]
    return t

def add_ownsbait(playerin,baitin,amountin):
    cb = OwnsBait.objects.get_or_create(player=playerin,bait=baitin,amount=amountin)
    return cb


if __name__ == '__main__':
    print "Starting Gofish population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','go_fish_project.settings')
    from gofish.models import Fish, Game, CaughtFish, Bait, Boat, Player, Trophy, OwnsBait
    from django.contrib.auth.models import User
    populate()
