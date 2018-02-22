""" Test task update """

from django.test import TestCase
from core.models import Process
from core.tasks import update

class UpdateTestCase(TestCase):
    """ Test task update """

    fixtures = ['auth.json', 'customers.json', 'processes.json']

    def setUp(self):
        process = Process.objects.get(pk=1)
        self.message = 'Message: O processo 123456, foi modificado.'
        self.result = update.delay(
            process.customer.webhook_url, process.process_number
        )
    
    def test_message(self):
        """ Verify if the message is correct """
        self.assertIn(self.message, self.result.get())
