""" Models """

from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """ Model for customers """
    user = models.ForeignKey(
        User, verbose_name='usuário', on_delete=models.CASCADE
    )
    webhook_url = models.CharField('url webhook', max_length=255)

    class Meta:
        """ Class meta """
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    def __str__(self):
        return self.user


class Process(models.Model):
    """ Model for processes """
    process_number = models.IntegerField('número do processo', max_length=20)
    process_data = models.TextField('dados do processo')
    customer = models.ForeignKey(
        Customer, verbose_name='cliente', on_delete=models.CASCADE
    )

    class Meta:
        """ Class meta """
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    def __str__(self):
        return self.process_number
