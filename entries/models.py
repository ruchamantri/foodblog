from django.contrib.auth.models import User
from django.db import models


class Entry(models.Model):
    entry_title = models.CharField(max_length=50)
    entry_text = models.TextField()
    entry_date = models.DateTimeField(auto_now_add=True)
    entry_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return f'{self.entry_title}'


class Contact(models.Model):
    contact_name = models.CharField(max_length=30)
    contact_email = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=20)
    contact_message = models.TextField(max_length=300)

