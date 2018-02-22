""" Enable django admin """

from django.contrib import admin
from core.models import Customer, Process
from core.tasks import update


class ProcessAdmin(admin.ModelAdmin):
    """ Customize Process Admin """
    def save_model(self, request, obj, form, change):
        super(ProcessAdmin, self).save_model(request, obj, form, change)
        update.delay(obj.customer.webhook_url, obj.process_number)


admin.site.register(Customer)
admin.site.register(Process, ProcessAdmin)
