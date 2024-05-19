from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Contact
from .forms import ContactForm
from .service import send


class ContactView(CreateView):

    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("contact")
    template_name = "main/contact.html"

    def form_valid(self, form):
        form.save()
        send(form.instance.email)
        return super().form_valid(form)
