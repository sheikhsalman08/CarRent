from django.shortcuts import render
from .models import Car,CarOwner
from .form import SearchForm
from django.views.generic import DetailView

# Create your views here.

def home(request):
	SmallCar = Car.objects.filter(seat__lte=5).order_by('-id')[:3]
	leargeCar = Car.objects.filter(seat__gte=6).order_by('-id')[:3]
	OfferCar = Car.objects.exclude(SpacialDiscount__isnull=True).exclude(SpacialDiscount="").exclude(availability=0).order_by('-id')[:4]
	Owners = CarOwner.objects.all()
	if request.method == 'POST':
		 Form = SearchForm(request.POST)
		 # print(SearchForm)
	else:
		Form = SearchForm


	context = {
		'SmallCar':SmallCar,
		'leargeCar':leargeCar,
		'OfferCar':OfferCar,
		'Owners':Owners,
		'SearchForm': Form
	}
	return render(request,'index.html',context)

def search(request):
	if request.method == 'POST':
		location = request.POST['location']
		model = request.POST['model']
		# result = Car.objects.filter(address_text__contains=location, model=model)
		result = Car.objects.filter(address_text__contains=location, model=model)

	else:
		result = ''

	context = {
		'SearchResult': result
	}
	return render(request,'search.html',context)

		
class SingleCar(DetailView):
	model = Car
	template_name = "order.html"

	def get_context_data(self, **kwargs):
		ThisCarId = self.kwargs['pk']
		ThisCar = Car.objects.get(id=ThisCarId)
		OfferCar = Car.objects.exclude(SpacialDiscount__isnull=True).exclude(SpacialDiscount="").order_by('-id')[:3]

		context = {
			'car' : ThisCar,
			'OfferCar':OfferCar,
		}

		return context