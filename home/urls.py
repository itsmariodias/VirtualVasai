from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('about/', views.AboutView.as_view(), name = "about"),
    path('regions/', views.RegionView.as_view(), name = "regions"),
]
