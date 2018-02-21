""" Test post in API """

from json import dumps
from django.test import TestCase


class TestProcessViewPost(TestCase):
    """ Test post in API """

    fixtures = ['auth.json', 'customers.json']

    def setUp(self):
        data = {
            'process_number': 123456789,
	        'process_data': 'Processo de teste 3',
	        'customer': 'admin'
        }

        self.response = self.client.post(
            '/api/process/', dumps(data),
            content_type='application/json'
        )

    def test_status_code(self):
        """ Check request status """
        self.assertEqual(201, self.response.status_code)

    def test_response_content_type(self):
        """ Check the submitted content type """
        self.assertEqual('application/json', self.response.get('Content-Type'))
