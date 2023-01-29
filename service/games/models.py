from django.db import models

import requests
import json


class Game(models.Model):
    name = models.CharField(max_length=100)
    links = models.CharField(max_length=100)
    RATE = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
    ]
    rate = models.IntegerField(choices=RATE, default=0)
    Country = models.CharField(max_length=100, null=True)
    About = models.TextField(max_length=500, null=True)

    def __str__(self):
        return f'{self.name}'


class SteamGames(models.Model):
    appid = models.TextField(null=True)
    name = models.TextField(null=True)

    def __str__(self):
        return f'{self.name}'


# requsts JSON
def parsedmessagelist():
    parsed_msg = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v2')
    if parsed_msg.status_code != 200:
        raise ConnectionError(parsed_msg.status_code)
    jsons = parsed_msg.json()['applist']
    for i in jsons['apps']:
        new_record = SteamGames(
            name=i['name'],
            appid=i['appid']
        )
        new_record.save()
    print('Ready!')


