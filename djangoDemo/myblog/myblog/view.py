from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    # return HttpResponse("Hello world hahhahah! ")
    content = {}
    content['hello'] = 'hello fjm'
    print content
    render(request,'hello.html',content)