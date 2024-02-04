from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def myview(request):
    return HttpResponse("<h1>Function based view</h1>")

class myclassview(View):
    name='sonam'
    def get(self,request):
        # return HttpResponse("<h1>Function Based View Get </h1>")
        return  HttpResponse(self.name)
    

class myclassviewchild(myclassview):
    def get(self,request):
        return HttpResponse(self.name)
       
    
    
    
