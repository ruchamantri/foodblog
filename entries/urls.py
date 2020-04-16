from django.urls import path
from .views import HomeView, EntryView, AboutMeView, ContactUsView, CreateRecipeView, RecipeEntryView, RecipeListView

urlpatterns = [
    path('', HomeView.as_view(), name = 'blog-home'),
    path('entry/<int:pk>/', EntryView.as_view(), name='post'),
    path('about/', AboutMeView.as_view(), name = 'about'),
    path('recipes/<int:pk>/', RecipeEntryView.as_view(), name='recipe_details'),
    path('recipes/', RecipeListView.as_view(), name='recipe_list'),
    path('submit/', CreateRecipeView.as_view(success_url='/recipes/'), name='submit_recipe'),
    path('contact/', ContactUsView.as_view(), name = 'contact_us')
]
