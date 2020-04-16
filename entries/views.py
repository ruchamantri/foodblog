from pydoc import render_doc

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import RecipeForm
from .models import Entry, Contact, Recipe


class HomeView(ListView):
    model = Entry
    template_name = 'entries/index.html'
    context_object_name = "blog_entries"
    ordering = ['-entry_date']

class EntryView(DetailView):
    model = Entry
    template_name = 'entries/post.html'

class RecipeListView(ListView):
    model = Recipe
    template_name = 'entries/recipes_list.html'
    context_object_name = "recipes_list"

class RecipeEntryView(DetailView):
    model = Recipe
    template_name = 'entries/recipes_details.html'
    context_object_name = "recipe_details"

class CreateRecipeView(CreateView):
    model = Recipe
    template_name = 'entries/submit_recipe.html'
    form_class = RecipeForm


    # def form_valid(self,form):
    #     print("hello")
    #     #.instance.author = self.request.user
    #     return super().form_valid(form)
    #
    # def post(self, request, *args, **kwargs):
    #     print("hello")
    #     return redirect('recipes_list')

class AboutMeView(ListView):
    model = Entry
    template_name = 'entries/about.html'

class ContactUsView(CreateView):
    model = Contact
    fields = '__all__'
    template_name = 'entries/contact.html'
