from django.contrib import admin
from .models import Car,CarOwner

# Register your models here.
admin.site.register(Car)
admin.site.register(CarOwner)

# class PointOfInterestAdmin(admin.ModelAdmin):
#     # list_display = ('model','seat')

#     def position_map(self, instance):
#         if instance.position is not None:
#             return '<img src="http://maps.googleapis.com/maps/api/staticmap?center=%(latitude)s,%(longitude)s&zoom=%(zoom)s&size=%(width)sx%(height)s&maptype=roadmap&markers=%(latitude)s,%(longitude)s&sensor=false&visual_refresh=true&scale=%(scale)s" width="%(width)s" height="%(height)s">' % {
#                 'latitude': instance.position.latitude,
#                 'longitude': instance.position.longitude,
#                 'zoom': 15,
#                 'width': 150,
#                 'height': 50,
#                 'scale': 2
#             }
#     position_map.allow_tags = True


# admin.site.register(Car, PointOfInterestAdmin)
# admin.site.register(CarOwner, PointOfInterestAdmin)
