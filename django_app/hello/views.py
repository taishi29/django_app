from django.shortcuts import render
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm

def index(request):
    data = Friend.objects.all().values()
    params = {
        'title':'Hello',
        'data': data,
    }
    return render(request, 'hello/index.html', params)

def create(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title':'Hello',
        'form':FriendForm(),
    }
    return render(request, 'hello/create.html', params)

'''
Friend()で、Friendモデルのインスタンスを作成。
FriendFormを使って、request.POSTをFriendインスタンスに設定する。
'''