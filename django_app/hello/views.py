from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    parms={
        'title': 'Hello/index',
        'msg': 'これは、サンプルで作ったページです'
    }
    return render(request, 'hello/index.html', parms)
# Create your views here.
