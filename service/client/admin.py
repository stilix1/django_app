from django.contrib import admin

from .models import *


@admin.register(Profile)
class GameAdmin(admin.ModelAdmin):
    filter_horizontal = ['games']


@admin.register(UserGameM)
class UserGameMAdmin(admin.ModelAdmin):
    pass