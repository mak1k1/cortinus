from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from store.models import Author, Book, Category, Product
from store.serializers import AuthorSerializer, BookSerializer, CategorySerializer, ProductSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Authors to be viewed or edited
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Authors to be viewed or edited
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Authors to be viewed or edited
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Authors to be viewed or edited
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# from django.shortcuts import render
# from django.views.generic import ListView, DetailView
# from .models import Product, Category
#
#
# class HomeView(ListView):
#     model = Product
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all()
#         return context
