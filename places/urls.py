from django.urls import path, reverse_lazy
from . import views

app_name='places'

urlpatterns = [
    path('', views.PlaceListView.as_view(), name='all'),
    path('<slug:slug>/', views.PlaceDetailView.as_view(), name="place_detail"),
    path('<slug:slug>/addreview/', views.addcomment, name='addcomment'),
    path('<slug:slug>/editreview/', views.editcomment, name='editcomment'),
]

# We use reverse_lazy in urls.py to delay looking up the view until all the paths are defined