# Generated by Django 3.2.16 on 2023-01-28 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20230128_2201'),
        ('client', '0002_auto_20230124_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergamem',
            name='steam_games',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='games.steamgames', verbose_name='Steam'),
        ),
        migrations.AlterField(
            model_name='usergamem',
            name='games',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='games.game', verbose_name='Игры'),
        ),
    ]
