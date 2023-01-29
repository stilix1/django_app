from django.contrib import admin
from ajax_select import make_ajax_form

from .models import *


@admin.register(Profile)
class GameAdmin(admin.ModelAdmin):
    filter_horizontal = ['games']
    search_fields = ['steam_games']
    show_full_result_count = 50


@admin.register(UserGameM)
class UserGameMAdmin(admin.ModelAdmin):
    raw_id_fields = ['steam_games']