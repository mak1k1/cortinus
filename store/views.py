from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Category


class HomeView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

