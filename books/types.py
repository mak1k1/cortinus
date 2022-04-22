from graphene_django.types import DjangoObjectType
from .models import Author, Book, Category


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

