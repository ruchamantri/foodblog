from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.TextField()
    method = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.recipe_name

