from django.contrib import admin
from .models import Coin, Minting

# Register your models here.
admin.site.register(Coin)
admin.site.register(Minting)