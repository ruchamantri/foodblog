# Generated by Django 3.0.2 on 2020-04-09 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0003_recipes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Recipes',
        ),
    ]