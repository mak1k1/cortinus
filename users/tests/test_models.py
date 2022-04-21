from django.contrib.auth import get_user_model
from django.test import TestCase
from users.models import Address


class UsersModelTests(TestCase):

    def test_creating_address(self):
        """Test creating address and its string representation"""
        address = Address.objects.create(
            full_name='Martin Cehelsky',
            street='Lincoln st',
            zip_code='12345',
            city='Honolulu',
            country='United States'
        )
        self.assertEqual(str(address), 'Lincoln st, 12345 Honolulu')

    def test_creating_user(self):
        """Test creating user and getting its name"""
        email = 'test@makiki.com'
        password = 'Password123'
        user = get_user_model().objects.create_user(
            email,
            password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))