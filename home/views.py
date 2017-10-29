from django.shortcuts import render
from .models import Car,CarOwner

# Create your views here.

def home(request):
	SmallCar = Car.objects.filter(seat__lte=6).order_by('-id')[:3]
	leargeCar = Car.objects.filter(seat__gte=5).order_by('-id')[:3]
	Owners = CarOwner.objects.all()

	context = {
		'SmallCar':SmallCar,
		'leargeCar':leargeCar,
		'Owners':Owners,

	}
	return render(request,'index.html')