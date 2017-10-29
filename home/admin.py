from django.contrib import admin
from .models import Car,CarOwner

# Register your models here.

admin.site.register(CarOwner)
admin.site.register(Car)
