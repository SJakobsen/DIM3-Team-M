import os

def populate():
    #populate_fish---------------------------------------------------------
    #reference from http://fogu.com/hm/animal_parade/fishing.php
    #size 20 = trophysize 10 = large, 5 = medium, 1 = small
    
    swordfishtr = add_fish('swordfish',500,20)
    
    #populate swordfish_trophy
    add_trophy('swordfish_trophy',swordfishtr)
    
    add_fish('swordfish',322,10)
    add_fish('swordfish',250,5)
    add_fish('swordfish',200,1)
    add_fish('char',99,10)
    add_fish('char',80,5)
    add_fish('char',60,1)
    add_fish('rainbow_trout',58,10)
    add_fish('rainbow_trout',40,5)
    add_fish('rainbow_trout',20,1)
    add_fish('masu_trout',109,10)
    add_fish('masu_trout',90,5)
    add_fish('masu_trout',70,1)
    add_fish('steelhead',72,10)
    add_fish('steelhead',60,5)
    add_fish('steelhead',40,1)
    add_fish('carp',59,10)
    add_fish('carp',40,5)
    add_fish('carp',30,1)
    
    eeltr = add_fish('eel',300,20)
    
    #populate eel_trophy
    add_trophy('eel_trophy',eeltr)
    
    add_fish('eel',198,10)
    add_fish('eel',170,5)
    add_fish('eel',140,1)
    add_fish('pond_smelt',7,10)
    add_fish('pond_smelt',5,5)
    add_fish('pond_smelt',3,1)
    add_fish('huchen',250,10)
    add_fish('huchen',220,5)
    add_fish('huchen',190,1)
    
    salmontr = add_fish('salmon',500,20)
    
    #populate salmon_trophy
    add_trophy('salmon_trophy',salmontr)
    
    add_fish('salmon',277,10)
    add_fish('salmon',240,5)
    add_fish('salmon',220,1)
    add_fish('catfish',106,10)
    add_fish('catfish',90,5)
    add_fish('catfish',60,1)
    add_fish('puffer',17,10)
    add_fish('puffer',13,5)
    add_fish('puffer',10,1)
    add_fish('goby',13,10)
    add_fish('goby',10,5)
    add_fish('goby',7,1)
    add_fish('sardine',17,10)
    add_fish('sardine',13,5)
    add_fish('sardine',10,1)
    add_fish('mahi-mahi',286,10)
    add_fish('mahi-mahi',250,5)
    add_fish('mahi-mahi',220,1)
    add_fish('horse_mackerel',81,10)
    add_fish('horse_mackerel',60,5)
    add_fish('horse_mackerel',40,1)
    add_fish('sea_bream',149,10)
    add_fish('sea_bream',110,5)
    add_fish('sea_bream',70,1)
    add_fish('bonito',120,10)
    add_fish('bonito',90,5)
    add_fish('bonito',70,1)
    add_fish('mackerel',85,10)
    add_fish('mackerel',70,5)
    add_fish('mackerel',60,1)
    add_fish('saury',92,10)
    add_fish('saury',70,5)
    add_fish('saury',50,1)
    add_fish('manta_ray',173,10)
    add_fish('manta_ray',130,5)
    add_fish('manta_ray',100,1)
    add_fish('rockfish',76,10)
    add_fish('rockfish',60,5)
    add_fish('rockfish',40,1)
    add_fish('cod',84,10)
    add_fish('cod',60,5)
    add_fish('cod',40,1)
    add_fish('angler_fish',330,10)
    add_fish('angler_fish',300,5)
    add_fish('angler_fish',290,1)
    add_fish('rock_trout',119,10)
    add_fish('rock_trout',90,5)
    add_fish('rock_trout',70,1)
    add_fish('yellowtail',153,10)
    add_fish('yellowtail',120,5)
    add_fish('yellowtail',90,1)
    
    tunatr = add_fish('tuna',500,20)
    
    #populate tuna_trophy
    add_trophy('tuna_trophy',tunatr)
    
    add_fish('tuna',317,10)
    add_fish('tuna',300,5)
    add_fish('tuna',280,1)
    add_fish('conger_eel',139,10)
    add_fish('conger_eel',110,5)
    add_fish('conger_eel',70,1)
    add_fish('halibut',125,10)
    add_fish('halibut',110,5)
    add_fish('halibut',90,1)
    add_fish('flounder',67,10)
    add_fish('flounder',70,5)
    add_fish('flounder',55,1)
    add_fish('squid',51,10)
    add_fish('squid',40,5)
    add_fish('squid',30,1)
    add_fish('octopus',60,10)
    add_fish('octopus',50,5)
    add_fish('octopus',40,1)
    add_fish('crawfish',7,10)
    add_fish('crawfish',4,5)
    add_fish('crawfish',3,1)
    add_fish('freshwater_prawn',23,10)
    add_fish('freshwater_prawn',20,5)
    add_fish('freshwater_prawn',17,1)
    add_fish('rock_lobster',91,10)
    add_fish('rock_lobster',75,5)
    add_fish('rock_lobster',60,1)
    add_fish('lobster',180,10)
    add_fish('lobster',160,5)
    add_fish('lobster',140,1)
    add_fish('shark',347,10)
    add_fish('shark',320,5)
    add_fish('shark',300,1)
    add_fish('skull_jellyfish',665,10)
    add_fish('skull_jellyfish',600,5)
    add_fish('skull_jellyfish',550,1)
    add_fish('giant_arowana',650,10)
    add_fish('giant_arowana',620,5)
    add_fish('giant_arowana',600,1)
    add_fish('barracuda',680,10)
    add_fish('barracuda',600,5)
    add_fish('barracuda',550,1)
    add_fish('tarpon',800,10)
    add_fish('tarpon',770,5)
    add_fish('tarpon',750,1)
    add_fish('dorado',700,10)
    add_fish('dorado',670,5)
    add_fish('dorado',650,1)
    add_fish('nautilus',830,10)
    add_fish('nautilus',800,5)
    add_fish('nautilus',780,1)
    add_fish('king_salmon',760,10)
    add_fish('king_salmon',740,5)
    add_fish('king_salmon',720,1)
    add_fish('giant_halibut',850,10)
    add_fish('giant_halibut',830,5)
    add_fish('giant_halibut',800,1)
    add_fish('brown_trout',79,10)
    add_fish('brown_trout',60,5)
    add_fish('brown_trout',50,1)
    add_fish('herring',76,10)
    add_fish('herring',60,5)
    add_fish('herring',50,1)

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
    add_bait('artificial_bait',10,1)
    add_bait('worm',20,4)
    add_bait('lob_worm',30,10)
    add_bait('rag_worm',50,12)
    add_bait('crayfish',100,20)
    add_bait('frog',150,20)
    add_bait('mud_lobster',200,50)

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


def add_fish(namein,pricein,sizein):
    f = Fish.objects.get_or_create(name=namein,price=pricein,size=sizein)[0]
    return f

def add_game(lakein,weatherin,playerin):
    g = Game.objects.get_or_create(lake=lakein,weather=weatherin,player=playerin)
    return g

def add_caughtfish(fishin,gamein,amountin):
    cf = CaughtFish.objects.get_or_create(fish=fishin,game=gamein,amount=amountin)
    return cf

def add_bait(namein,qualityin,pricein):
    b = Bait.objects.get_or_create(name=namein,quality=qualityin,price=pricein)
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
