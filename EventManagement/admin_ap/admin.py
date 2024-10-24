from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Event)
admin.site.register(Service)
admin.site.register(Pricing)
admin.site.register(Review)
admin.site.register(Booking)