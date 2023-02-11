from django.db import models

import requests
import json


class SteamGames(models.Model):
    name = models.TextField(null=True)
    appid = models.TextField(null=True)

    def __str__(self):
        return f'{self.name}'


# requsts JSON
def parsed_steam_games():
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


