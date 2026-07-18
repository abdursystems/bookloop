from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('new/', views.create_listing, name='create_listing'),
]
