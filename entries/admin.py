from django.contrib import admin

from recipes.models import Recipe
from .models import Entry

admin.site.register(Entry)
admin.site.register(Recipe)