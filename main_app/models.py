from django.db import models
from django.urls import reverse

# Create your models here.
class Coin(models.Model):
    type = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    year_released = models.IntegerField()
    date_of_statehood = models.IntegerField()

def __str__(self):
    return f'{self.name} ({self.id})'

def get_absolute_url(self):
    return reverse('detail', kwargs={'coin_id': self.id})