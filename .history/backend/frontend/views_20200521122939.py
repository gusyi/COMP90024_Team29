from django.shortcuts import render
from tweets.models import TweetResultData, City

# Create your views here.

def home(request):

    return render(request, 'frontend/home.html')

def index(request):
    context = {
        'queryset' : TweetResultData.objects.all(),
        'City': City.objects.all(),
    }
    return render(request, 'frontend/index.html')

def map(request):
    return render(request, 'frontend/map.html')

def city(request, city_id):
    context = {
        'city_id' : city_id
    }
    
    return render(request, 'frontend/city.html', context = context)
