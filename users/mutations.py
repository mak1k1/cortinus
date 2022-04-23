from audioop import add
from re import A
import graphene
from .models import Address, User
from .types import AddressType, UserType


class CreateUserMutation(graphene.Mutation):
    class Arguments:
        """Input arguments for editing User"""
        email = graphene.String()
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
        is_staff = graphene.Boolean(required=False)
        avatar = graphene.String(required=False)
        addresses = graphene.List(graphene.ID, required=False)

    user = graphene.Field(UserType)

    def mutate(self, info, email, **kwargs):

        first_name = kwargs.get('first_name', "")
        last_name = kwargs.get('last_name', "")
        is_staff = kwargs.get('is_staff', False)
        avatar = kwargs.get('avatar', None)
        addresses = kwargs.get('addresses', [])

        user = User.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            avatar=avatar,
        )
        user.addresses.set(addresses)

        user.save()
        return CreateUserMutation(user=user)


class EditUserMutation(graphene.Mutation):
    class Arguments:
        """Input arguments for editing User"""
        id = graphene.ID(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, id, **kwargs):
        email = kwargs.get('email', None)
        first_name = kwargs.get('first_name', None)
        last_name = kwargs.get('last_name', None)
        is_staff = kwargs.get('is_staff', None)
        avatar = kwargs.get('avatar', None)
        addresses = kwargs.get('addresses', None)

        user = User.objects.get(pk=id)

        if email is not None:
            user.email = email

        if first_name is not None:
            user.first_name = first_name

        if last_name is not None:
            user.last_name = last_name

        if is_staff is not None:
            user.is_staff = is_staff

        if avatar is not None:
            user.avatar = avatar

        if addresses is not None:
            user.addresses = addresses

        user.save()
        return EditUserMutation(user=user)
