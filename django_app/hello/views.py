from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params={
        'title': 'Hello/index',
        'msg': 'これは、サンプルで作ったページです',
        'goto': 'next',
    }
    return render(request, 'hello/index.html', params)


def next(request):
    params={
        'title': 'Hello/Next',
        'msg' : 'これは、もう一つのページだよ',
        'goto' : 'index',
    }
    return render(request, 'hello/index.html/', params)

# Create your views here.
