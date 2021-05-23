from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from django.contrib import admin
from django.urls import reverse


class AdminSiteTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_super_user(
            email='admin111@devl.com',
            password='Admin123'
        )

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test222@devl.com',
            password='Test123',
            name='Test User Full Name'
        )

    def test_users_listed(self):
        """ Test that users are listed on Users Page """

        """ self.setUp() """

        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
