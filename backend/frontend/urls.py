from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name="index"),
    path('map/', views.map, name="map"),
    path('city/<int:city_id>/', views.city, name="city"),
]
