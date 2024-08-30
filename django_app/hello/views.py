from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm

class HelloView(TemplateView):
    
    def __init__(self):
        self.params = {
            'title' : 'Hello!',
            'message' : 'your data:',
            'form' : HelloForm(),
            'result' : None
        }
    
    def get(self, request):
        return render(request, 'hello/index.html', self.params)
    
    def post(self, request):
        ch = request.POST.getlist('choice')
        result = '<ol class="list-group"><b>selected:</b>'
        for item in ch:
            result += '<li class="list-group-item">' + item + '</li>'
        result +='</ol>'
        self.params['result'] = result
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)
        

