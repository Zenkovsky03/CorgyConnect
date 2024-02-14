from django.urls import path
from . import views

urlpatterns = [
    path('', views.dogs, name='dogs'),
    path('dog/<str:pk>/', views.dog, name='dog')
]
