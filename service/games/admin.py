from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(SteamGames)
class SteamGamesAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'appid',
    ]
    search_fields = ['name']
    show_full_result_count = 50
