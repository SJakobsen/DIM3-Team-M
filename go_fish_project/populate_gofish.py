import os

def populate():



def add_fish(namein,pricein,sizein):
    f = Fish.objects.get_or_create(name=namein,price=pricein,size=sizein)
    return f

def add_game(lakein,weatherin):
    g = Game.objects.get_or_create(lake=lakein,weather=weatherin)
    return g

def add_containfish(fishin,gamein,amountin):
    cf = Containfish.get_or_create(fish=fishin,game=gamein,amount=amountin)
    return cf

def add_bait(namein,qualityin):
    b = Bait.get_or_create(name=namein,quality=qualityin)
    return b

def add_boat(namein,speedin):
    b = Boat.get_or_create(name=namein,speed=speedin)
    return b

def add_player(usernamein,passwordin,namein,rankingin,moneyin)
    

if __name__ == '__main__':
    print "Starting Gofish population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','go_fish_project.settings')
    from gofish.models import Fish, Game, Containfish, Bait, Boat, Player, Trophy
    populate()
