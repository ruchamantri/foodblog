from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):
    image = forms.ImageField(label="Upload Image", help_text="")

    class Meta:
        model = Recipe
        fields = "__all__"
