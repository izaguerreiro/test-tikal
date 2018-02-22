""" Test delete in API """

from django.test import TestCase


class TestProcessViewPost(TestCase):
    """ Test delete in API """

    fixtures = ['auth.json', 'customers.json', 'processes.json']

    def setUp(self):
        self.response = self.client.delete(
            '/api/process/1/', content_type='application/json'
        )

    def test_status_code(self):
        """ Check request status """
        self.assertEqual(204, self.response.status_code)
