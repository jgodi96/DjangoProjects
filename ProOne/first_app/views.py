from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(response):
    my_dict = {'insert_me':"Hello I am from view.py !"}
    return render(request,'index.html',context=my_dict)
