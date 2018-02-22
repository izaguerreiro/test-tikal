""" Test models process """

from django.contrib.auth.models import User
from django.test import TestCase
from core.models import Customer, Process


class TestModelProcess(TestCase):
    """ Test Models Process """
    def setUp(self):
        self.user = User.objects.create_user(
            'maria', 'maria@maria.com', '1234'
        )
        self.customer = Customer.objects.create(
            user=self.user, webhook_url='maria.com'
        )
        self.process = Process.objects.create(
            process_number=123456,
            process_data='Atraso no pagamento', customer=self.customer
        )

    def test_create(self):
        """ Checks if a process exists  """
        self.assertTrue(Process.objects.exists())

    def test_process_number(self):
        """ Checks if process number is correct """
        self.assertEqual(123456, self.process.process_number)

    def test_process_data(self):
        """ Checks if process data is correct """
        self.assertEqual('Atraso no pagamento', self.process.process_data)

    def test_customer(self):
        """ Checks if customer is correct """
        self.assertEqual(self.customer, self.process.customer)
