""" Views file """

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.serializer import ProcessSerializer
from core.models import Customer, Process


def list_process(request, customer):
    """ Lists customer processes """
    context = {}
    customer = Customer.objects.get(user__username=customer)
    context['processes'] = Process.objects.filter(customer=customer)
    context['customer'] = customer
    return render(request, 'processes.html', context)
