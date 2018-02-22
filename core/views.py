""" Views file """

from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.serializer import ProcessSerializer
from core.models import Customer, Process


def home(request):
    return redirect('/admin/')

def list_process(request, customer):
    """ Lists customer processes """
    context = {}
    customer = Customer.objects.get(user__username=customer)
    context['processes'] = Process.objects.filter(customer=customer)
    context['customer'] = customer
    return render(request, 'processes.html', context)


class ProcessView(APIView):
    serializer_class = ProcessSerializer

    def get_object(self, pk):
        try:
            return Process.objects.get(pk=pk)
        except Process.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        serializer = self.serializer_class(Process.objects.all(), many=True)
        return Response(serializer.data)        

    def post(self, request, format=None):
        customer = Customer.objects.get(
            user__username=request.data['customer'])
        data = {
            'customer': customer.pk,
            'process_number': request.data['process_number'],
            'process_data': request.data['process_data']
        }
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        process = self.get_object(pk)
        process.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        