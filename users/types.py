from graphene_django.types import DjangoObjectType
from .models import User, Address


class UserType(DjangoObjectType):
    class Meta:
        model = User

class AddressType(DjangoObjectType):
    class Meta:
        model = Address