from django.db import models

# Create your models here.

class Car(models.Model):
	image = models.FileField(null = True, blank = True )
	choices = (
		(u'1',u'Perodua Myvi'),
		(u'2',u'Perodua Alza'),
		(u'3',u'Perodua Axia'),
		(u'4',u'Honda City'),
		(u'5',u'Honda Civic'),
		# ('1','Instagram'),('2','facebook'),('3','youtube')
	)
	model = models.CharField(max_length = 40, blank = True, null = True,choices = choices )
	seat = models.IntegerField(default=5)
	ac =  models.BooleanField(default=True)
	availability =  models.BooleanField(default=True)
	owner = models.ForeignKey('CarOwner',blank = False, null = False, related_name="car_owner")
	address = models.CharField(max_length = 240, blank = True, null = True)
	per_hour = models.IntegerField(default=10)
	SpacialDiscount = models.CharField(max_length = 240, blank = True, null = True)

class CarOwner(models.Model):
	name = models.CharField(max_length = 240, blank = True, null = True)
	number = models.CharField(max_length = 40, blank = True, null = True)
	whatsAppN = models.CharField(max_length = 40, blank = True, null = True)
	email = models.EmailField(max_length=254)
	image = models.FileField(null = True, blank = True )
	address = models.CharField(max_length = 240, blank = True, null = True)