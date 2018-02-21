""" Api to create and delete processes """

from rest_framework import serializers
from core.models import Customer, Process


class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = '__all__'
