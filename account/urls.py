from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name='account'

urlpatterns = [
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path("register/", views.register, name="register"),
]