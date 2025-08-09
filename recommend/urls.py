from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # home page
    path('get_weather/', views.get_weather, name='get_weather'),  # your weather function
]
