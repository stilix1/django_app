# Generated by Django 3.2.16 on 2023-01-28 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20230128_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='steamgames',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]