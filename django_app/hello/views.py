from django.shortcuts import render
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm
from django.views.generic import ListView
from django.views.generic import DetailView

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

def edit(request, num):
    obj = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title':'Hello',
        'id': num,
        'form':FriendForm(instance=obj),
        ## instance=obj をフォームに渡すことで、そのインスタンスに含まれるデータがフォームの初期値として表示されます。
    }
    return render(request, 'hello/edit.html', params)

def delete(request, num):
    friend = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    params = {
        'title':'Hello',
        'id': num,
        'obj': friend,
        ## instance=obj をフォームに渡すことで、そのインスタンスに含まれるデータがフォームの初期値として表示されます。
    }
    return render(request, 'hello/delete.html', params)

class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend
    
    
'''
Friend()で、Friendモデルのインスタンスを作成。
FriendFormを使って、request.POSTをFriendインスタンスに設定する。
'''