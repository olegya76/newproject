from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse

def index(request):
    my_dict={'insert_me':"Hello I am from testapp/index.html"}
    return render(request,'testapp/index.html',context=my_dict)
