# Create your views here.
from django.views.generic import CreateView, ListView, DetailView

from entries.models import Entry
from recipes.forms import RecipeForm
from recipes.models import Recipe


class CreateRecipeView(CreateView):
    model = Recipe
    form_class = RecipeForm

class RecipeListView(ListView):
    model = Recipe
    template_name = 'entries/recipes_list.html'
    context_object_name = "recipes_list"

class RecipeEntryView(DetailView):
    model = Recipe
    template_name = 'entries/recipes_details.html'
    context_object_name = "recipe_details"

