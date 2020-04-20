from pydoc import render_doc

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Entry, Contact


class HomeView(ListView):
    model = Entry
    template_name = 'entries/index.html'
    context_object_name = "blog_entries"
    ordering = ['-entry_date']

class EntryView(DetailView):
    model = Entry
    template_name = 'entries/post.html'

class AboutMeView(ListView):
    model = Entry
    template_name = 'entries/about.html'

class ContactUsView(CreateView):
    model = Contact
    fields = '__all__'
    template_name = 'entries/contact.html'
