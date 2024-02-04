from django.shortcuts import render
from django.views import View
from .forms import ContactForm 
from django.http import HttpResponse
# Create your views here.
def homefun(request):
    return render(request,'school/home.html')


class HomeclassView(View):
    def get(self,request):
        return render(request,'school/home.html')


def aboutfun(request,template_name):
  
    context={"msg":"hey there this is prerak"}
    return render(request,template_name,context)


class aboutclass(View):
    def get(self,request):
        context={"msg":"hey there this is prerak patel speaking"}
        return render(request,'school/about.html',context)
    
    
    
    
def contactfun(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse("Thankyou form submittewd")
        
    else:
        form=ContactForm()
    return render(request,'school/contact.html',{'form':form})



class ContactClass(View):
    def get(self,request):
        form=ContactForm()
        return render(request,'school/contact.html',{'form':form})

    def post(self,request):
        form =ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('ThankYou form submitted')
        
        
def newsfun(request,template_name):
    # template_name='school/news.html'
    template_name=template_name
    context={'info':'where does this money comes from'} 
    return render(request,template_name,context)     
        
    
class newsclass(View):
    # template_name='school/news.html'
    template_name=''
    def get(self,request):
        context={'info':'where does this money comes from'} 
        return render(request,self.template_name,context)     
        