# ====================================
# COMP90024 Cluster and Cloud Computing - Assignment 2
# Group 29
# Hongwei Yin 901012
# Cheng Sun 900806
# Xinyi Xu 900966
# Yiran Yao 1144268
# Xiaotao Tan 1032950
# ====================================
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name="index"),
    path('map/', views.map, name="map"),
    path('city/<int:city_id>/', views.city, name="city"),
]
