from django.contrib import admin

# Register your models here.

from .models import Location,Collection,Comic

admin.site.register(Location)
admin.site.register(Collection)
admin.site.register(Comic)
