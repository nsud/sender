import threading
from datetime import datetime

from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic import ListView

from app.models import Mess, SendTo


class ListMessage(ListView):
    model = Mess
    context_object_name = 'msgs'
    template_name = 'email_list.html'
    queryset = Mess.objects.order_by('-id')[:10]


class ListEmail(ListView):
    model = SendTo
    context_object_name = 'msgs'
    template_name = 'email_addr.html'
    queryset = SendTo.objects.all()


def add_email(request):
    if request.method == 'POST':
        message = request.POST['message']
        sec = int(request.POST['time']) if request.POST['time'] != '' else 0
        msg = Mess(title=f"Message - {datetime.now()}", body=message, status=2)
        msg.save()
        t = threading.Timer(sec, send_email, args=(message, msg))
        t.start()

    return render(request, 'create_email.html', {})


def send_email(message, msg):
    msg.status = 1
    msg.save()
    send_mail('Contact Form',
                message,
                settings.EMAIL_HOST_USER,
                [mails.mail for mails in SendTo.objects.all()],
                fail_silently=False)
