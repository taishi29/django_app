from django.shortcuts import render
from .models import Friend
from django.db.models import QuerySet


def __new_str__(self):
    result = ''
    for item in self:
        result += '<tr>'
        for k in item:
            result += '<td>' + str(k) + '=' + str(item[k]) + '</td>'
        result += '</tr>'
    return result 

QuerySet.__str__ = __new_str__

def index(request):
    data = Friend.objects.all().values('id', 'name', 'age')
    params = {
        'title':'Hello',
        'data': data,
    }
    return render(request, 'hello/index.html', params)

'''
__str__とは、Pythonにおいてオブジェクトを文字列として表示する際に呼び出される特殊メソッドである。
例えば、print()関数を使ってオブジェクトを出力する場合や、str()関数でオブジェクトを文字列に変換する際に、
__str__メソッドが自動的に呼ばれる。
具体的には、print()関数やstr()関数を使ってオブジェクトを文字列として表示しようとすると、
この__str__メソッドが呼び出され、そのオブジェクトがどのように文字列として表示されるかが定義されている。

このカスタムメソッド__new_str__は、QuerySetオブジェクトをHTMLのテーブル形式で表示しようとしている。
'''