from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Contact
from .forms import ContactForm
from .service import send
from .tasks import send_spam_email


class ContactView(CreateView):

    model = Contact
    form_class = ContactForm
    success_url = "contact"
    template_name = "main/contact.html"

    def form_valid(self, form):
        form.save()

        # <название таски> .delay (параметры) запуск таски через celery
        # send_spam_email.delay(form.instance.email)

        send_spam_email.delay(3)
        return super().form_valid(form)
