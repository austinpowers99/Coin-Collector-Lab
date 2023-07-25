from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def coins_index(request):
    return render(request, 'coins/index.html', {
        'coins': coins
})

coins = [
    {'type': 'Quarter', 'state': 'California', 'year_released': 2005, 'date_of_statehood': 1850}
]