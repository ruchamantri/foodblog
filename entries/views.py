from django.views.generic import ListView, DetailView, CreateView

from .models import Entry


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
