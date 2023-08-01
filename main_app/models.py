from django.db import models
from django.urls import reverse
from datetime import date
# from django.contrib.auth.models import User

MINT_MARK = (
    ('D', 'Denver'),
    ('P', 'Philadelphia'),
    ('S', 'San Francisco')
)

class Material(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('materials_detail', kwargs={'pk': self.id})

class Coin(models.Model):
    type = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    year_released = models.IntegerField()
    date_of_statehood = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'coin_id': self.id})

class Minting(models.Model):
    date = models.DateField('Date added to this collection')
    mint_mark = models.CharField(
        max_length=1,
        choices=MINT_MARK,
        default=MINT_MARK[0][0]
    )

    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_mint_mark_display()} on {self.date}"
    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    cat = models.ForeignKey(Coin, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for coin_id: {self.coin_id} @{self.url}"
