from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
class HomeTemplateView(TemplateView):
    template_name='school/home.html'