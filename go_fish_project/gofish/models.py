from django.db import models

# Create your models here.
class Fish(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    size = models.DecimalField(max_digits=6, decimal_places=4)

    def __unicode__(self):
        return "name: "+self.name+" price: "+str(self.price)+" size: "+str(self.size)

class Bait(models.Model):
    name = models.CharField(max_length=30)
    quality = models.IntegerField()
    price = models.DecimalField(max_digits=12,decimal_places=2)
    
    def __unicode__(self):
        return "name: "+self.name+" quality: "+str(self.quality)+" price: "+str(self.price)

class Boat(models.Model):
    name = models.CharField(max_length=30)
    speed = models.IntegerField()
    price = models.DecimalField(max_digits=12,decimal_places=2)
    
    def __unicode__(self):
        return "name: "+self.name+" speed: "+str(self.speed)+" price: "+str(self.price)

class Player(models.Model):
    username = models.CharField(max_length=12,unique=True)
    password = models.CharField(max_length=12,unique=True)
    name = models.CharField(max_length=12,unique=True)
    ranking = models.IntegerField()
    money = models.DecimalField(max_digits=12,decimal_places=2)
    boat = models.ForeignKey(Boat,blank=True,null=True)
    bait = models.ManyToManyField(Bait, through = 'Containbait')
    
    def __unicode__(self):
        return "name: "+self.name+" ranking: "+str(self.ranking)+" money: "+str(self.money)

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
    fish = models.ManyToManyField(Fish, through = 'Containfish')
    player = models.OneToOneField(Player)

    def __unicode__(self):
        return "lake: "+self.lake+" weather: "+self.weather+" played by username: "+self.player.username

class CaughtFish(models.Model):
    fish = models.ForeignKey(Fish)
    game = models.ForeignKey(Game)
    amount = models.IntegerField()

    def __unicode__(self):
        return "fish: "+str(self.fish)+" game: "+str(self.game)+" amount: "+str(self.amount)




