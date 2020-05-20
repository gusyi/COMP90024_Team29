from django.shortcuts import render
from tweets.models import TweetResultData

# Create your views here.

def home(request):

    return render(request, 'frontend/home.html')

def index(request):
    model = TweetResultData
    query_set = TweetResultData.objects.all()
    return render(request, 'frontend/index.html')

def map(request):
    return render(request, 'frontend/map.html')

def city(request, city_id):
    context = {
        'city_id' : city_id
    }
    
    return render(request, 'frontend/city.html', context = context)
