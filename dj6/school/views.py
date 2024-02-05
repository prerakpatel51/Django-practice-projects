from typing import Any
from django.shortcuts import render

# Create your views here.
from .models import Student
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView



class StudentDetailView(DetailView):
    model=Student
    template_name='school/index.html'
    context_object_name='student'
    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['all']=self.model.objects.all()
        return context

class StudentListView(ListView):
    model=Student
    template_name='school/home.html'
    context_object_name='students'
    
    
    
    
        