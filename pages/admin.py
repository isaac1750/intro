from django.contrib import admin

# Register your models here.
from .models import City
from .models import Contact

class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "state",)

class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "message", "name",)

admin.site.register(City, CityAdmin)
admin.site.register(Contact, ContactAdmin)
