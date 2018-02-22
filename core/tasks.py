""" Tasks file """

from celery import shared_task


@shared_task
def update(webhook, process):
    message = """
        To: {} 
        Message: O processo {}, foi modificado.
    """.format(webhook, process)
    print(message)
    return message