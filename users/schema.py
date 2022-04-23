import graphene

from users.mutations import CreateAddressMutation, CreateUserMutation, EditUserMutation
from .models import Address, User
from .types import AddressType, UserType


class Query(graphene.ObjectType):
    address = graphene.Field(AddressType, address_id=graphene.Int())
    addresses = graphene.List(AddressType)

    user = graphene.Field(UserType, user_id=graphene.Int())
    users = graphene.List(UserType)

    def resolve_address(self, info, address_id):
        return Address.objects.get(pk=address_id)

    def resolve_user(self, info, user_id):
        return User.objects.get(pk=user_id)

    def resolve_addresses(self, info, **kwargs):
        return Address.objects.all().order_by('-full_name')

    def resolve_users(self, info, **kwargs):
        return User.objects.all().order_by('-date_joined')


class Mutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()
    update_user = EditUserMutation.Field()
    create_address = CreateAddressMutation.Field()


schema = graphene.Schema(query=Query)
