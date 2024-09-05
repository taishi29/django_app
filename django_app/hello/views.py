from django.shortcuts import render
from .models import Friend
from .forms import HelloForm

def index(request):
    num = Friend.objects.all().count()
    first = Friend.objects.all().first()
    last = Friend.objects.all().last()
    data = [num, first, last]
    params = {
        'title':'Hello',
        'data': data,
    }
    return render(request, 'hello/index.html', params)

'''
all():QuerySetというクラスのインスタンスとしてレコードの値が取り出される。
count()メソッド:取得したレコードの数を返す
first()メソッド:allの中の、最初のものだけを返す
last()メソッド:allの中の、最後のものだけを返す
'''