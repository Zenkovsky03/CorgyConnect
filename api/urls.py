from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('', views.getRoutes),

    path('dogs/', views.getDogs),
    path('dogs/<str:pk>/', views.getDog),
    path('dogs/<str:pk>/vote/', views.dogVote),

    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('remove-tag/', views.removeTag),
]