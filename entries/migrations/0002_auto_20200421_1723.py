# Generated by Django 3.0.2 on 2020-04-21 11:53

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='_entry_text_excerpt',
            field=models.TextField(default=django.utils.timezone.now, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entry',
            name='entry_text',
            field=model_utils.fields.SplitField(no_excerpt_field=True),
        ),
    ]
