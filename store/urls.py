from django.contrib import admin
from django.urls import path, include
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view()),
    path('<slug:category_slug>', HomeView.as_view())
]
