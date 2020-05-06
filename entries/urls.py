from django.urls import path

from recipes.views import RecipeEntryView, RecipeListView
from .views import HomeView, EntryView, AboutMeView

urlpatterns = [
    path('', HomeView.as_view(), name = 'blog-home'),
    path('entry/<int:pk>/', EntryView.as_view(), name='post'),
    path('about/', AboutMeView.as_view(), name = 'about'),
    path('recipes/<int:pk>/', RecipeEntryView.as_view(), name='recipe_details'),
    path('recipes/', RecipeListView.as_view(), name='recipe_list'),
]
