from django.shortcuts import render
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm
from django.views.generic import ListView
from django.views.generic import DetailView
from .forms import FindForm
from .forms import CheckForm
from django.core.paginator import Paginator

def index(request, num=1):
    data = Friend.objects.all()
    page = Paginator(data, 2)
    params = {
        'title':'Hello',
        'message':'',
        'data': page.get_page(num),
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
    
def find(request):
    if(request.method == 'POST'):
        form = FindForm(request.POST)
        find = request.POST['find']
        data = Friend.objects.filter(age__lte=int(find))
        msg = 'Result: ' + str(data.count())
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title':'Hello',
        'message':msg,
        'form':form,
        'data':data,
    }
    return render(request, 'hello/find.html', params)

def check(request):
    params = {
        'title': 'Hello',
        'message': 'check validation.',
        'form': CheckForm(),
    }
    if request.method == "POST":
        form = CheckForm(request.POST)
        params['form'] = form
        if form.is_valid(): 
            params['message'] = 'OK!'
        else:
            params['message'] = 'no good.'
    return render(request, 'hello/check.html', params)


'''
Friend()で、Friendモデルのインスタンスを作成。
FriendFormを使って、request.POSTをFriendインスタンスに設定する。
'''