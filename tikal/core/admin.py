""" Enable django admin """

from django.contrib import admin
from core.models import Customer, Process


class ProcessInline(admin.TabularInline):
    """ Create a tabular inline """
    model = Process
    extra = 1


class CustomerAdmin(admin.ModelAdmin):
    """ Add tabular inline on customer """
    inlines = [ProcessInline]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Process)
