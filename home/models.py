from django.db import models
from geoposition.fields import GeopositionField

# Create your models here.

class Car(models.Model):
	image = models.FileField(null = True, blank = True )
	choices = (
		(u'Perodua Myvi',u'Perodua Myvi'),
		(u'Perodua Alza',u'Perodua Alza'),
		(u'Perodua Axia',u'Perodua Axia'),
		(u'Honda City',u'Honda City'),
		(u'Honda Civic',u'Honda Civic'),
		(u'Hyundai Sonata',u'Hyundai Sonata'),
		# ('1','Instagram'),('2','facebook'),('3','youtube')
	)
	model = models.CharField(max_length = 40, blank = True, null = True,choices = choices )
	seat = models.IntegerField(default=5)
	ac =  models.BooleanField(default=True)
	availability =  models.BooleanField(default=True)
	owner = models.ForeignKey('CarOwner',blank = False, null = False, related_name="car_owner")
	address = GeopositionField(blank = True, null = True)
	address_text = models.CharField(max_length = 240, blank = True, null = True)
	per_hour = models.IntegerField(default=10)
	per_day = models.IntegerField(default=10)
	SpacialDiscount = models.CharField(max_length = 240, blank = True, null = True)

	def __str__(self):
		return "{} by {}".format(self.model,self.owner)

class CarOwner(models.Model):
	name = models.CharField(max_length = 240, blank = True, null = True)
	number = models.CharField(max_length = 40, blank = True, null = True)
	whatsAppN = models.CharField(max_length = 40, blank = True, null = True)
	email = models.EmailField(max_length=254)
	image = models.FileField(null = True, blank = True )
	address = models.CharField(max_length = 240, blank = True, null = True)
	address_text = GeopositionField(blank = True, null = True)

	def __str__(self):
		return self.name
