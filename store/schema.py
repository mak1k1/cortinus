import graphene

from store.mutations import CreateLanguageMutation, CreateOrderMutation, UpdateLanguageMutation, UpdateOrderMutation
from .models import Language, Order, OrderItem, Product, Publisher
from .types import LanguageType, OrderType, OrderItemType, ProductType, PublisherType


class Query(graphene.ObjectType):
    language = graphene.Field(LanguageType, language_id=graphene.Int())
    languages = graphene.List(LanguageType)

    order = graphene.Field(OrderType, order_id=graphene.Int())
    orders = graphene.List(OrderType)

    orderitem = graphene.Field(OrderItemType, orderitem_id=graphene.Int())
    orderitems = graphene.List(OrderItemType)

    product = graphene.Field(ProductType, product_id=graphene.Int())
    products = graphene.List(ProductType)

    publisher = graphene.Field(PublisherType, publisher_id=graphene.Int())
    publishers = graphene.List(PublisherType)

    def resolve_language(self, info, language_id):
        return Language.objects.get(pk=language_id)

    def resolve_order(self, info, order_id):
        return Order.objects.get(pk=order_id)

    def resolve_orderitem(self, info, orderitem_id):
        return OrderItem.objects.get(pk=orderitem_id)

    def resolve_product(self, info, product_id):
        return Product.objects.get(pk=product_id)

    def resolve_publisher(self, info, publisher_id):
        return Publisher.objects.get(pk=publisher_id)

    def resolve_languages(self, info, **kwargs):
        return Language.objects.all().order_by('-name')

    def resolve_orders(self, info, **kwargs):
        return Order.objects.all().order_by('-created_at')

    def resolve_orderitems(self, info, **kwargs):
        return OrderItem.objects.all().order_by('-added_at')

    def resolve_products(self, info, **kwargs):
        return Product.objects.all().order_by('-price')

    def resolve_publishers(self, info, **kwargs):
        return Publisher.objects.all().order_by('-name')


class Mutation(graphene.ObjectType):
    create_language = CreateLanguageMutation.Field()
    update_language = UpdateLanguageMutation.Field()
    create_order = CreateOrderMutation.Field()
    update_order = UpdateOrderMutation.Field()


schema = graphene.Schema(query=Query)
