from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Coin

# Create your views here.
coins = [
    {'type': 'Quarter', 'state': 'California', 'year_released': 2005, 'date_of_statehood': 1850}
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def coins_index(request):
    return render(request, 'coins/index.html', {
        'coins': coins
})

def coins_index(request):
    coins = Coin.objects.all()
    return render(request, 'coins/index.html', { 'coins': coins })

def coins_detail(request, coin_id):
    coin = Coin.objects.get(id=coin_id)
    return render(request, 'coins/detail.html', { 'coin': coin })

class CoinCreate(CreateView):
    model = Coin
    fields = '__all__'
    success_url = '/coins/{coin_id}'

class CoinUpdate(UpdateView):
    model = Coin
    field = ['type', 'state', 'year_released', 'date_of_statehood']

class CoinDelete(DeleteView):
    model = Coin
    success_url = '/coins'