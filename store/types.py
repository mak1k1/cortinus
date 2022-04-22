from graphene_django.types import DjangoObjectType
from .models import Language, Order, OrderItem, Product, Publisher


class LanguageType(DjangoObjectType):
    class Meta:
        model = Language


class OrderType(DjangoObjectType):
    class Meta:
        model = Order


class OrderItemType(DjangoObjectType):
    class Meta:
        model = OrderItem


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class PublisherType(DjangoObjectType):
    class Meta:
        model = Publisher
