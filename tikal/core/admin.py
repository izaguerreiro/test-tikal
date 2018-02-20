""" Enable django admin """

from django.contrib import admin
from core.models import Customer, Process


admin.site.register(Customer)
admin.site.register(Process)
