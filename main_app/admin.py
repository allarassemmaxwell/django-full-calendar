from django.contrib import admin
from .models import *
# Register your models here.

# LANGUAGE ADMIN
class EventsAdmin(admin.ModelAdmin):
    list_display        = ['name', 'start', 'end']
    list_display_links  = ['name',]
    list_filter         = ['name']
    search_fields       = ['name']
    list_per_page       = 25
    class Meta:
        model = Events
admin.site.register(Events, EventsAdmin)


