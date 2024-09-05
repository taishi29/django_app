from django.shortcuts import render
from django.shortcuts import redirect
from .models import Friend
from .forms import HelloForm


def index(request):
    data = Friend.objects.all().values()
    params = {
        'title':'Hello',
        'data': data,
    }
    return render(request, 'hello/index.html', params)

def create(request):
    params = {
        'title':'Hello',
        'form': HelloForm(),
    }
    if (request.method == 'POST'):
        name = request.POST['name']
        mail = request.POST['mail']
        gender = 'gender' in request.POST
        age = request.POST['age']
        birth = request.POST['birthday']
        friend = Friend(name=name, mail=mail, gender=gender, age=age, birthday=birth)
        friend.save()
        return redirect(to='/hello')
    return render(request, 'hello/create.html', params)
