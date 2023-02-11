# Generated by Django 3.2.16 on 2023-02-11 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_auto_20230211_0550'),
        ('games', '0004_auto_20230128_2201'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.AddField(
            model_name='steamgames',
            name='links',
            field=models.TextField(default='https://store.steampowered.com/app/<django.db.models.fields.TextField>/'),
        ),
    ]
