from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Contact
from .forms import ContactForm


class ContactView(CreateView):

    model = Contact
    form_class = ContactForm
    success_url = "/"
    template_name = "main/contact.html"

    def form_valid(self, form):
        form.save()
        send(form.instance.email)
        return super().form_valid(form)
