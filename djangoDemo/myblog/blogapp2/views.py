from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'blogapp2/index.html')
    # return HttpResponse('hello,world')
