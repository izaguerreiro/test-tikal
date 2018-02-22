""" Validators """

from django.core.exceptions import ValidationError


def validate_process_number(value):
    """ Validade process number """
    if not value.isdigit():
        raise ValidationError(
            'O número do processo deve conter apenas números', 'digits')

    if len(value) != 20:
        raise ValidationError(
            'O número do processo deve ter 20 números', 'length')