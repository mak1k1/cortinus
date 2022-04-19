from django.test import TestCase
from books.models import Author

class BooksModelsTests(TestCase):



    def test_creating_author(self):
        """Test creating Actor is successful"""
        author = Author.objects.create(
            name='Martin Cehelsky',
            description='Best author ever'
        )
        self.assertEqual(str(author), author.name)
