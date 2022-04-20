from django.test import TestCase
from books.models import Author, Category, Book
from store.models import Language, Product, Publisher


class StoreModelsTests(TestCase):

    def setUp(self):

        self.book = Book.objects.create(
            title='A book',
            isbn='1234567890123',
            pages=420,
            description='A sample book',
        )

        self.book.authors.set([Author.objects.create(
            name='Martin Cehelsky',
            description='Sample Author'
        )])
        self.book.categories.set([Category.objects.create(
            name='Fiction',
            description='Fiction books'
        )])


    def test_creating_language(self):
        """Test creating Language is successful and string representation is returned"""
        language = Language.objects.create(
            code='en-us',
            name='English - United states'
        )
        self.assertEqual(str(language), language.name)

    def test_creating_publisher(self):
        """Test creating Publisher is successful and string representation is returned"""
        publisher = Publisher.objects.create(
            name='Publisher',
            description='Top american book publisher'
        )
        self.assertEqual(str(publisher), publisher.name)

    def test_creating_product(self):
        """Test creating Product is successful and string representation is returned"""
        product = Product.objects.create(
            price = 14.99,
            language = Language.objects.create(code='sk', name='Slovak'),
            publisher = Publisher.objects.create(name='publisher', description='publisher description'),
            book = self.book,
            stock_count = 15,
        )
        self.assertEqual(str(product), str(product.book))
