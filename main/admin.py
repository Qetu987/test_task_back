from django.contrib import admin
from .models import Servis, Subservice

# Register your models here.
@admin.register(Servis)
class ServisAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    list_search = ['id', 'name']


@admin.register(Subservice)
class SubserviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'servises_id', 'name', 'price', 'date']
    list_display_links = ['id','servises_id', 'name', 'price']
    list_search = ['id', 'servises_id', 'name']
    list_filter = ['servises_id']