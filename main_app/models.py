from django.db import models
from django.urls import reverse
from datetime import date

MINT_MARK = (
    ('D', 'Denver'),
    ('P', 'Philadelphia'),
    ('S', 'San Francisco')
)

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