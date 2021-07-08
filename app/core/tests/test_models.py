from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Check if creating user with email is successful"""
        email = 'test@checkdjango.com'
        password = 'Test1234'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Check if while creating a user, email is normalized"""
        email = 'martand@DEVEL.COM'
        user = get_user_model().objects.create_user(email, 'TEST1234')

        self.assertEqual(user.email, email.lower())

    def test_new_userinvalid_email(self):
        """ Test creating user with no email raises error """

        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(None, 'Test123')

    def test_create_super_user(self):
        """ Test Creating Super User   """
        user = get_user_model().objects.create_super_user('admin@devel.com',
                                                          'admin123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
