""" Test models customer """

from django.contrib.auth.models import User
from django.test import TestCase
from core.models import Customer


class TestModelCustomer(TestCase):
    """ Test Model Customer """
    def setUp(self):
        self.user = User.objects.create_user(
            'maria', 'maria@maria.com', '1234'
        )
        self.customer = Customer.objects.create(
            user=self.user, webhook_url='maria.com'
        )

    def test_create(self):
        """ Checks if a customer exists  """
        self.assertTrue(Customer.objects.exists())

    def test_user(self):
        """ Checks if user is correct """
        self.assertEqual(self.user, self.customer.user)

    def test_webhook_url(self):
        """ Checks if webhook is correct """
        self.assertEqual('maria.com', self.customer.webhook_url)
