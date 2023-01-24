from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from games.models import Game


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    nickname = models.CharField(max_length=80, blank=True)
    total_games = models.CharField(max_length=30, blank=True, default=0)
    total_h = models.CharField(max_length=30, blank=True, default=0)
    birth_date = models.DateField(null=True, blank=True)
    games = models.ManyToManyField(Game)

    def __str__(self):
        return f'{self.user} - {self.nickname}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class UserGameM(models.Model):
    games = models.ForeignKey(Game, on_delete=models.PROTECT, verbose_name='Игра')
    client = models.ForeignKey(Profile, on_delete=models.PROTECT, verbose_name='Пользователь')
    user_rate = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(10),
    ],
        verbose_name='Оценка')
    user_h = models.IntegerField(verbose_name='Часов в игре', default=0)
    user_review = models.TextField(blank=True, verbose_name='Отзыв')

    def __str__(self):
        return f'User: {self.client} || Game: {self.games}'
