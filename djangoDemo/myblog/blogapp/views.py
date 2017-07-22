from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from . import  models
def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blogapp/index.html', {'articles': articles })

    # article = models.Article.objects.get(pk=1)
    # return render(request, 'blogapp/index.html', {'article': article })

    # return render(request,'blogapp/index.html')
    # return HttpResponse('hello,world')
