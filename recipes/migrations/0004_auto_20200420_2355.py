# Generated by Django 3.0.2 on 2020-04-20 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20200420_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='name',
            new_name='recipe_name',
        ),
    ]
