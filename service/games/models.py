from django.db import models


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
    rate = models.IntegerField(choices=RATE)
    Country = models.CharField(max_length=100)
    About = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.name}'




