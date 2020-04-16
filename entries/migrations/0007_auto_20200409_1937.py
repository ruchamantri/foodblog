# Generated by Django 3.0.2 on 2020-04-09 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0006_auto_20200409_1933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_ingredients',
            new_name='ingredients',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_method',
            new_name='method',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_name',
            new_name='name',
        ),
    ]