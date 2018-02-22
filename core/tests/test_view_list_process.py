""" Test view list process """

from django.shortcuts import resolve_url as r
from django.test import TestCase


class TestViewListProcess(TestCase):
    """ Test view list process """

    fixtures = ['auth.json', 'customers.json', 'processes.json']

    def setUp(self):
        self.response = self.client.get(r('customer-process', 'admin'))

    def test_get(self):
        """ Checks request status """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Checks if template used is correct """
        self.assertTemplateUsed(self.response, 'processes.html')
