import graphene
from graphql_jwt.decorators import staff_member_required, login_required

from .models import Language, Order, OrderItem, Product, Publisher
from users.models import User
from books.models import Book
from .types import LanguageType, OrderType, OrderItemType, ProductType, PublisherType

class CreateLanguageMutation(graphene.Mutation):
    """Input arguments for creating Language"""
    class Arguments:
        code = graphene.String()
        name = graphene.String()

    language = graphene.Field(LanguageType)

    @staff_member_required
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

    @staff_member_required
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

    @login_required
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

    @staff_member_required
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

    @staff_member_required
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

    @staff_member_required
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


class CreateProductMutation(graphene.Mutation):
    """Input arguments for creating Publisher"""
    class Arguments:
        price = graphene.String()
        language_id = graphene.Int(name='language')
        publisher_id = graphene.Int(name='publisher')
        book_id = graphene.Int(name='book')
        stock_count = graphene.Int()

    product = graphene.Field(ProductType)

    @staff_member_required
    def mutate(self, info, price, language_id, publisher_id, book_id, stock_count):
        try:
            language = Language.objects.get(pk=language_id)
        except Language.DoesNotExist:
            language = None

        try:
            publisher = Publisher.objects.get(pk=publisher_id)
        except Publisher.DoesNotExist:
            publisher = None

        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            book = None

        product = Product.objects.create(
            price=price,
            language=language,
            publisher=publisher,
            book=book,
            stock_count=stock_count,
        )
        return CreateProductMutation(product=product)


class UpdateProductMutation(graphene.Mutation):
    """Input arguments for updating Product"""
    class Arguments:
        id = graphene.ID()
        price = graphene.String(required=False)
        language_id = graphene.Int(required=False, name='language')
        publisher_id = graphene.Int(required=False, name='publisher')
        book_id = graphene.Int(required=False, name='book')
        stock_count = graphene.Int(required=False)

    product = graphene.Field(ProductType)

    @staff_member_required
    def mutate(self, info, id, **kwargs):
        price = kwargs.get('price', None)
        language_id = kwargs.get('language_id', None)
        publisher_id = kwargs.get('publisher_id', None)
        book_id = kwargs.get('book_id', None)
        stock_count = kwargs.get('stock_count', None)

        product = Product.objects.get(pk=id)

        if price is not None:
            product.price = price

        if stock_count is not None:
            product.stock_count = stock_count

        if language_id is not None:
            try:
                language = Language.objects.get(pk=language_id)
            except Language.DoesNotExist:
                language = None
            product.language = language

        if publisher_id is not None:
            try:
                publisher = Publisher.objects.get(pk=publisher_id)
            except Publisher.DoesNotExist:
                publisher = None
            product.publisher = publisher

        if book_id is not None:
            try:
                book = Book.objects.get(pk=book_id)
            except Book.DoesNotExist:
                book = None
            product.book = book

        product.save()
        return UpdateProductMutation(product=product)


class CreateOrderItemMutation(graphene.Mutation):
    """Input arguments for creating OrderItem"""
    class Arguments:
        product_id = graphene.Int(name='product')
        order_id = graphene.Int(name='order')
        qty = graphene.Int()
        image = graphene.String()

    orderitem = graphene.Field(OrderItemType)

    @login_required
    def mutate(self, info, product_id, order_id, qty,  image):
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            product = None

        try:
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            order = None

        orderitem = OrderItem.objects.create(
            qty=qty,
            image=image,
            product=product,
            order=order
        )

        return CreateOrderItemMutation(orderitem=orderitem)


class UpdateOrderItemMutation(graphene.Mutation):
    """Input arguments for updating OrderItem"""
    class Arguments:
        id = graphene.ID()
        product_id = graphene.Int(name='product', required=False)
        order_id = graphene.Int(name='order', required=False)
        qty = graphene.Int(required=False)
        image = graphene.String(required=False)

    orderitem = graphene.Field(OrderItemType)

    @login_required
    def mutate(self, info, id, **kwargs):
        product_id = kwargs.get('product_id', None)
        order_id = kwargs.get('order_id', None)
        qty = kwargs.get('qty', None)
        image = kwargs.get('image', None)

        orderitem = OrderItem.objects.get(pk=id)

        if qty is not None:
            orderitem.qty = qty

        if image is not None:
            orderitem.image = image

        if product_id is not None:
            try:
                product = Product.objects.get(pk=product_id)
            except Product.DoesNotExist:
                product = None
            orderitem.product = product

        if order_id is not None:
            try:
                order = Order.objects.get(pk=order_id)
            except Order.DoesNotExist:
                order = None
            orderitem.order = order


        orderitem.save()
        return UpdateOrderItemMutation(orderitem=orderitem)