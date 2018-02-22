""" Test view home """

from django.shortcuts import resolve_url as r
from django.test import TestCase


class TestViewHome(TestCase):
    """ Test view home """

    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        """ Checks request status """
        self.assertEqual(302, self.response.status_code)
