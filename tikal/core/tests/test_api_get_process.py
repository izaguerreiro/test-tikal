""" Test get in API """

from django.test import TestCase


class TestProcessViewPost(TestCase):
    """ Test get in API """

    fixtures = ['auth.json', 'customers.json', 'processes.json']

    def setUp(self):
        self.response = self.client.get(
            '/api/process/', content_type='application/json'
        )

    def test_status_code(self):
        """ Check request status """
        self.assertEqual(200, self.response.status_code)
