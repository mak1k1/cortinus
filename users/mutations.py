import graphene
from graphql_jwt.decorators import login_required

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

    user = graphene.Field(UserType)

    @login_required
    def mutate(self, info, email, **kwargs):

        first_name = kwargs.get('first_name', "")
        last_name = kwargs.get('last_name', "")
        is_staff = kwargs.get('is_staff', False)
        avatar = kwargs.get('avatar', None)

        user = User.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            avatar=avatar,
        )

        user.save()
        return CreateUserMutation(user=user)


class UpdateUserMutation(graphene.Mutation):
    class Arguments:
        """Input arguments for editing User"""
        id = graphene.ID(required=True)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
        is_staff = graphene.Boolean(required=False)
        avatar = graphene.String(required=False)

    user = graphene.Field(UserType)

    @login_required
    def mutate(self, info, id, **kwargs):
        email = kwargs.get('email', None)
        first_name = kwargs.get('first_name', None)
        last_name = kwargs.get('last_name', None)
        is_staff = kwargs.get('is_staff', None)
        avatar = kwargs.get('avatar', None)

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

        user.save()
        return UpdateUserMutation(user=user)


class CreateAddressMutation(graphene.Mutation):
    class Arguments:
        """Input arguments for creating Address"""
        full_name = graphene.String()
        street = graphene.String()
        zip_code = graphene.String()
        city = graphene.String()
        country = graphene.String()
        user_id = graphene.Int(required=True, name='user')

    address = graphene.Field(AddressType)

    @login_required
    def mutate(self, info, full_name, street, zip_code, city, country, user_id):
        user = User.objects.get(pk=user_id)
        address = Address.objects.create(
            full_name=full_name,
            street=street,
            zip_code=zip_code,
            city=city,
            country=country,
            user=user
        )

        return CreateAddressMutation(address=address)


class UpdateAddressMutation(graphene.Mutation):
    class Arguments:
        """Input arguments for editing Address"""
        id = graphene.ID(required=True)
        full_name = graphene.String(required=False)
        street = graphene.String(required=False)
        zip_code = graphene.String(required=False)
        city = graphene.String(required=False)
        country = graphene.String(required=False)

    address = graphene.Field(AddressType)

    @login_required
    def mutate(self, info, id, **kwargs):
        full_name = kwargs.get('full_name', None)
        street = kwargs.get('street', None)
        zip_code = kwargs.get('zip_code', None)
        city = kwargs.get('city', None)
        country = kwargs.get('country', None)

        address = Address.objects.get(pk=id)

        if full_name is not None:
            address.full_name = full_name

        if street is not None:
            address.street = street

        if zip_code is not None:
            address.zip_code = zip_code

        if city is not None:
            address.city = city

        if country is not None:
            address.country = country

        address.save()
        return UpdateAddressMutation(address=address)
