from django.shortcuts import render
from .models import Friend
from .forms import HelloForm

def index(request):
    data = Friend.objects.all()
    params = {
        'title':'Hello',
        'data': data,
    }
    return render(request, 'hello/index.html', params)
