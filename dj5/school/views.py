from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student
# Create your views here.
class StudentListView(ListView):
    model=Student
    
# if we were not using this we needed to write this three line of the code here by default we get the student_list object in the html file 
# stud=Student.object.all()
# context={'student_list':stud}
# return render(request,'school/student_list.html',context)
    
class StudentListview1(ListView):
    model=Student
    # template_name_suffix=''# this will search for student.html instead of student_list.html
    template_name='school/student.html'
    ordering=['name']
    context_object_name='students'
    
    def get_queryset(self):
        return Student.objects.filter(course='Python')
    
    def get_context_data(self,*args, **kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['freshers']=Student.objects.all().order_by('name')
        return context
    
    def get_template_names(self):
        if self.request.COOKIES['user']=='sila':
            template_name='school/sila.html'
        else:
            template_name=self.template_name
        return [template_name]