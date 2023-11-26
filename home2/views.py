from django.shortcuts import render
from django.views.generic import ListView
from home2.models import Home2

class Home2(ListView):
    model = Home2
    template_name = 'templates/home2.html'




