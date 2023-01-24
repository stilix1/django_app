# Generated by Django 3.2.16 on 2023-01-24 19:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=80)),
                ('total_games', models.CharField(blank=True, default=0, max_length=30)),
                ('total_h', models.CharField(blank=True, default=0, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('games', models.ManyToManyField(to='games.Game')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserGameMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_rate', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Оценка')),
                ('user_h', models.IntegerField(default=0, verbose_name='Часов в игре')),
                ('user_review', models.TextField(blank=True, verbose_name='Отзыв')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.profile', verbose_name='Пользователь')),
                ('games', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='games.game', verbose_name='Игра')),
            ],
        ),
    ]
