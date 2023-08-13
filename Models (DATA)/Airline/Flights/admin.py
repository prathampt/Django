from django.contrib import admin

from .models import flight,airport,passanger
# Register your models here.

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class PassangerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flight",)

admin.site.register(flight, FlightAdmin)
admin.site.register(airport)
admin.site.register(passanger, PassangerAdmin)
