from django.db import models

# Create your models here.

class Fish(models.Model):
	name = models.CharField(max_length=128)
	rarity = models.CharField(max_length=10)
	sell_price = models.DecimalField(max_digits=9, decimal_places=2)
	class Meta:
		unique_together = ("name","rarity")	
	
	def __unicode__(self):
		return "name:"+self.name+" rarity:"+self.rarity+" price:"+str(self.sell_price)


class Item(models.Model):
	name = models.CharField(max_length=128,unique=True)
	rarity = models.CharField(max_length=10)
	sell_price = models.DecimalField(max_digits=9, decimal_places=2)	
	description = models.CharField(max_length=128)
	
#inherit Item
class Fishhook(Item):
	quality = models.IntegerField()
	def __unicode__(self):
                return "name:"+self.name+" rarity:"+self.rarity+" price:"+str(self.sell_price)

class Fishingboat(Item):
	quality = models.IntegerField()
        def __unicode__(self):
                return "name:"+self.name+" rarity:"+self.rarity+" price:"+str(self.sell_price)

class Bait(Item):
	quality = models.IntegerField()
	def __unicode__(self):
                return "name:"+self.name+" rarity:"+self.rarity+" price:"+str(self.sell_price)

class Place(models.Model):
	name = models.CharField(max_length=128,unique=True)
	rarity = models.CharField(max_length=10)
	level_need = models.IntegerField()
	boatquality_need = models.IntegerField()
	fish = models.ManyToManyField(Fish)

	def __unicode__(self):
                return "name:"+self.name+" rarity:"+self.rarity

class Trophy(models.Model):
	type = models.CharField(max_length=10)
	def __unicode__(self):
                return "type: "+self.type

class User(models.Model):
	username = models.CharField(max_length = 10,unique=True)
	password = models.CharField(max_length = 10,unique=True)
	name = models.CharField(max_length = 10,unique=True)
	rank = models.IntegerField()
	level = models.IntegerField()
	money = models.DecimalField(max_digits=12, decimal_places=2)
	trophy = models.ManyToManyField(Trophy, through='Containtrophy')
        fishhook = models.ManyToManyField(Fishhook)
	fishingboat = models.ManyToManyField(Fishingboat)
	bait = models.ManyToManyField(Bait, through='Containbait')
	fish = models.ManyToManyField(Fish, through='Containfish')
        def __unicode__(self):
		return "name: "+self.name+" username: "+self.username+"level: "+str(self.level)

class Shop(models.Model):
	name = models.CharField(max_length = 20)
	fishhook = models.ManyToManyField(Fishhook)
        fishingboat = models.ManyToManyField(Fishingboat)
        bait = models.ManyToManyField(Bait)
	def __unicode__(self):
		return "name: "+self.name

class Containfish(models.Model):
	fish = models.ForeignKey(Fish)
	user = models.ForeignKey(User)
	amount = models.IntegerField()
	def __unicode__(self):
		return "USER:"+self.user.name+"//Contain:"+self.fish.name+"//Amount:"+str(self.amount)

class Containbait(models.Model):
	bait = models.ForeignKey(Bait)
	user = models.ForeignKey(User)
	amount = models.IntegerField()
	def __unicode__(self):
                return "USER:"+self.user.name+"//Contain:"+self.bait.name+"//Amount:"+str(self.amount)

class Containtrophy(models.Model):
	trophy = models.ForeignKey(Trophy)
	user = models.ForeignKey(User)
	amount = models.IntegerField()
        def __unicode__(self):
                return "USER:"+self.user.name+"//Contain:"+self.trophy.type+"//Amount:"+str(self.amount)
 

