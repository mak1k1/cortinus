import graphene
from .models import Language, Order, OrderItem, Product, Publisher
from users.models import User
from .types import LanguageType, OrderType, OrderItemType, ProductType, PublisherType


class CreateLanguageMutation(graphene.Mutation):
    """Input arguments for creating Language"""
    class Arguments:
        code = graphene.String()
        name = graphene.String()
    
    language = graphene.Field(LanguageType)

    def mutate(self, info, code, name):
        language = Language.objects.create(
            code=code,
            name=name
        )
        return CreateLanguageMutation(language=language)

class UpdateLanguageMutation(graphene.Mutation):
    """Input arguments for updating Language"""
    class Arguments:
        id = graphene.ID()
        code = graphene.String(required=False)
        name = graphene.String(required=False)

    language = graphene.Field(LanguageType)

    def mutate(self, info, id, **kwargs):
        code = kwargs.get('code', None)
        name = kwargs.get('name', None)

        language = Language.objects.get(pk=id)

        if code is not None:
            language.code = code

        if name is not None:
            language.name = name


        language.save()
        return UpdateLanguageMutation(language=language)


class CreateOrderMutation(graphene.Mutation):
    """Input arguments for creating Language"""
    class Arguments:
        user_id = graphene.Int(required=False, name='user')
    
    order = graphene.Field(OrderType)

    def mutate(self, info, **kwargs):
        try:
            user_id = kwargs.get('user_id', None)
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            user = None

        order = Order.objects.create(
            user=user
        )
        return CreateOrderMutation(order=order)


class UpdateOrderMutation(graphene.Mutation):
    """Input arguments for updating Language"""
    class Arguments:
        id = graphene.ID()
        shipping_price = graphene.String(required=False)
        tax_price = graphene.String(required=False)
        user_id = graphene.Int(required=False, name='user')
        is_paid = graphene.Boolean(required=False)
        is_delivered = graphene.Boolean(required=False)

    order = graphene.Field(OrderType)

    def mutate(self, info, id, **kwargs):
        shipping_price = kwargs.get('shipping_price', None)
        tax_price = kwargs.get('tax_price', None)
        is_paid = kwargs.get('is_paid', None)
        is_delivered = kwargs.get('is_delivered', None)
        user_id = kwargs.get('user', None)

        order = Order.objects.get(pk=id)

        if shipping_price is not None:
            order.shipping_price = shipping_price

        if tax_price is not None:
            order.tax_price = tax_price

        if is_paid is not None:
            order.is_paid = is_paid

        if is_delivered is not None:
            order.is_delivered = is_delivered

        if user_id is not None:
            try:
                user = User.objects.get(pk=user_id)
            except User.DoesNotExist:
                user = None

            order.user = user
            

        order.save()
        return UpdateOrderMutation(order=order)


class CreatePublisherMutation(graphene.Mutation):
    """Input arguments for creating Publisher"""
    class Arguments:
        name = graphene.String()
        description = graphene.String()
    
    publisher = graphene.Field(PublisherType)

    def mutate(self, info, name, description):
        publisher = Publisher.objects.create(
            name=name,
            description=description
        )
        return CreatePublisherMutation(publisher=publisher)

class UpdatePublisherMutation(graphene.Mutation):
    """Input arguments for updating Publisher"""
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=False)
        description = graphene.String(required=False)

    publisher = graphene.Field(PublisherType)

    def mutate(self, info, id, **kwargs):
        name = kwargs.get('name', None)
        description = kwargs.get('description', None)

        publisher = Publisher.objects.get(pk=id)

        if description is not None:
            publisher.description = description

        if name is not None:
            publisher.name = name


        publisher.save()
        return UpdatePublisherMutation(publisher=publisher)
