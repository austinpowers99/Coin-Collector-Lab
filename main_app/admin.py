from django.contrib import admin
from .models import Coin, Minting, Material, Photo

# Register your models here.
admin.site.register(Coin)
admin.site.register(Minting)
admin.site.register(Material)
admin.site.register(Photo)