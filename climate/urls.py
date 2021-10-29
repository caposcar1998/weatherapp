from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),


    path('<str:country>/weather/', views.weather, name="weather"),
    path('<str:country>/days/', views.days, name="days")
]