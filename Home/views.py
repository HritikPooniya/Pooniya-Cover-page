from multiprocessing import context
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):#context is onlyfor knowledge wedont used in to sent this in this type.
    context = {
        "variable1": "this is the value of first variable",
        "variable2":"this is the vlaue of second variale"


    }
    

    return render(request,'index.html',context)#context is the dictionary which is used to sent the values with keys.
    #return HttpResponse('this is homepage')

def about(request):
    return render(request,'about.html',)
   # return HttpResponse('this is about page')

def services(request):
    return render(request,'services.html',)
    #return HttpResponse('this is service page')
    def Icecream(request):
        return render(request,'service.html')

def contact(request):
    return render(request,'contact.html',)
    #return HttpResponse('this is contact page')