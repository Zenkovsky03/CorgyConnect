from django.urls import path
from . import views
urlpatterns = [
    path('', views.getRoutes),
    path('dogs/', views.getDogs),
    path('dogs/<str:pk>/', views.getDog),
]