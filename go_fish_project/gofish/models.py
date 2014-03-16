from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Fish(models.Model):
    name = models.CharField(max_length=64)
    base_price = models.IntegerField()
    base_chance = models.IntegerField()

    # fish size vars, used to determine the actual size
    size_mean = models.DecimalField(max_digits=8,decimal_places=2)
    size_sd = models.DecimalField(max_digits=8,decimal_places=2)
    weight_mean = models.DecimalField(max_digits=8,decimal_places=2)
    weight_sd = models.DecimalField(max_digits=8,decimal_places=2)

    # chance to cache parameters enhancers
    # that can go into negative
    p_depth = models.IntegerField()
    p_bsize = models.IntegerField()
    # that are always positive
    p_clouds = models.IntegerField()
    p_rain = models.IntegerField()
    p_wind = models.IntegerField()

    def __unicode__(self):
        return "name: "+self.name+", base_price: "+str(self.base_price)+", base_chance: "+str(self.base_chance)+", and more stuff"

class Bait(models.Model):
    name = models.CharField(max_length=30)
    colour = models.IntegerField() # mate or bright
    size = models.IntegerField() # 0-4
    price = models.IntegerField()
    
    def __unicode__(self):
        return "name: "+self.name+" colour: "+str(self.colour)+" size: " + str(self.size) + " price: "+str(self.price)

class Boat(models.Model):
    name = models.CharField(max_length=30)
    speed = models.IntegerField()
    price = models.DecimalField(max_digits=12,decimal_places=2)
    
    def __unicode__(self):
        return "name: "+self.name+" speed: "+str(self.speed)+" price: "+str(self.price)

class Player(models.Model):
    user = models.OneToOneField(User)
    
    ranking = models.IntegerField()
    money = models.DecimalField(max_digits=12,decimal_places=2)
    boat = models.ForeignKey(Boat,blank=True,null=True)
    bait = models.ManyToManyField(Bait, through = 'OwnsBait')
    
    def __unicode__(self):
        return "name: "+self.user.username+" ranking: "+str(self.ranking)+" money: "+str(self.money)

class OwnsBait(models.Model):
    player = models.ForeignKey(Player)
    bait = models.ForeignKey(Bait)
    amount = models.IntegerField()

    def __unicode__(self):
        return "player: "+str(self.player)+" bait: "+str(self.bait)+" amount: "+str(self.amount)

class Trophy(models.Model):
    name = models.CharField(max_length=30)
    fish = models.ForeignKey(Fish)
    player = models.ForeignKey(Player,blank=True,null=True)
    
    def __unicode__(self):
        return "name: "+self.name+" for fish: "+str(self.fish)+" player: "+str(self.player)

class Game(models.Model):
    lake = models.CharField(max_length=30)
    weather = models.CharField(max_length=30)
    fish = models.ManyToManyField(Fish, through = 'CaughtFish')
    player = models.OneToOneField(Player)

    def __unicode__(self):
        return "lake: "+self.lake+" weather: "+self.weather+" played by username: "+self.player.username

class CaughtFish(models.Model):
    fish = models.ForeignKey(Fish)
    game = models.ForeignKey(Game)
    size = models.IntegerField()
    weight = models.DecimalField(max_digits=8,decimal_places=2)
    price = models.IntegerField()
	
    def __unicode__(self):
        return "fish: "+str(self.fish)+" game: "+str(self.game)+" size: "+str(self.size)+" weight: "+str(self.weight)+" price: "+str(self.price)
