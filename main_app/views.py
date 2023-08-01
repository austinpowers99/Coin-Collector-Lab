import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Coin, Material, Photo
from .forms import MintingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def coins_index(request):
    coins = Coin.objects.all()
    return render(request, 'coins/index.html', { 'coins': coins })

@login_required
def coins_detail(request, coin_id):
    coin = Coin.objects.get(id=coin_id)
    minting_form = MintingForm()
    return render(request, 'coins/detail.html', { 
        'coin': coin, 'minting_form': minting_form
    })

@login_required
def add_minting(request, coin_id):
    form = MintingForm(request.POST)
    # validate the form
    if form.is_valid():
    # don't save the form to the db until it
    # has the coin_id assigned
        new_minting = form.save(commit=False)
        new_minting.coin_id = coin_id
        new_minting.save()
    return redirect('detail', coin_id=coin_id)

class CoinCreate(CreateView):
    model = Coin
    fields = '__all__'
    success_url = '/coins'

class CoinUpdate(UpdateView):
    model = Coin
    fields = ['type', 'state', 'year_released', 'date_of_statehood']
class CoinDelete(DeleteView):
    model = Coin
    success_url = '/coins/'

class MaterialList(LoginRequiredMixin, ListView):
    model = Material

class MaterialDetail(LoginRequiredMixin, DetailView):
    model = Material

class MaterialCreate(LoginRequiredMixin, CreateView):
    model = Material
    fields = '__all__'

class MaterialUpdate(LoginRequiredMixin, UpdateView):
    model = Material
    fields = ['name']

class MaterialDelete(LoginRequiredMixin, DeleteView):
    model = Material
    success_url = '/materials'

@login_required
def assoc_material(request, coin_id, material_id):
    Coin.objects.get(id=coin_id).materials.add(material_id)
    return redirect('detail', coin_id=coin_id)

@login_required
def unassoc_material(request, coin_id, material_id):
    Coin.objects.get(id=coin_id).materials.remove(material_id)
    return redirect('detail', coin_id=coin_id)

@login_required
def add_photo(request, coin_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
        bucket = os.environ['S3_BUCKET']
        s3.upload_fileobj(photo_file, bucket, key)
        url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
        Photo.objects.create(url=url, coin_id=coin_id)
    except Exception as e:
        print('An error occurred uploading file to S3')
        print(e)
    return redirect('detail', coin_id=coin_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
        # Save the user to the db
            user = form.save()
        login(request, user)
        return redirect('index')
    else:
        error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)