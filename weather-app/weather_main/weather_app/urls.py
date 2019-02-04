from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('weather/', views.WeatherPageView.as_view(), name='weather'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('api/', views.WeatherAPI.as_view()),
]
