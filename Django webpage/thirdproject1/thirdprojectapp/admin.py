from django.contrib import admin

# Register your models here.
from . models import place,members

admin.site.register(place)
admin.site.register(members)