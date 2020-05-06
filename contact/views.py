
from django.shortcuts import render

from .forms import ContactForm

def success(request):
    template = "success.html"
    context = 'success'

def contact(request):
    template = "contact.html"

    if request.method =="POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'success.html')

    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render (request, template, context)

