from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, 'frontend/home.html')

def index(request):

    return render(request, 'frontend/index.html')