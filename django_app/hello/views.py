from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from .forms import SessionForm
from .models import Friend

def index(request):
    data = Friend.objects.all()
    params = {
        'title':'Hello',
        'massage':'all friends.',
        'data':data,
    }
    return render(request, 'hello/index.html', params)
