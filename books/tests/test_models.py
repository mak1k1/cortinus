from django.test import TestCase
from books.models import Author, Category, Book


class BooksModelsTests(TestCase):

    def test_creating_author(self):
        """Test creating Actor is successful"""
        author = Author.objects.create(
            name='Martin Cehelsky',
            description='Best author ever'
        )
        self.assertEqual(str(author), author.name)

    def test_creating_category(self):
        """Test creating Category is successful"""
        category = Category.objects.create(
            name='Fiction',
            description='Fiction books'
        )
        self.assertEqual(str(category), category.name)

    def test_creating_book(self):
        """Test Many to Many relationship by creating Book with authors and categories"""
        author1 = Author.objects.create(
            name='Martin Cehelsky',
            description='Sample Author'
        )

        author2 = Author.objects.create(
            name='Martin Nehelsky',
            description='Sample Author'
        )

        category1 = Category.objects.create(
            name='Non-Fiction',
            description='Non-Fiction books'
        )

        category2 = Category.objects.create(
            name='Fiction',
            description='Fiction books'
        )

        book = Book.objects.create(
            title='A book',
            isbn='1234567890123',
            pages=420,
            description='A sample book',
        )

        book.authors.set([author1, author2])
        book.categories.set([category1, category2])

        self.assertEqual(str(book), book.title)
        self.assertEqual(len(book.categories.all()), 2)
        self.assertEqual(len(book.authors.all()), 2)
        self.assertEqual(book.authors.first().name,author1.name)
        self.assertEqual(book.categories.first().name, category1.name)
