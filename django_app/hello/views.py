from django.shortcuts import render
from .models import Friend
from .forms import HelloForm

def index(request):
    data = Friend.objects.all().values_list('id', 'name')
    params = {
        'title':'Hello',
        'data': data,
    }
    return render(request, 'hello/index.html', params)

'''
【モデルオブジェクト】
データベーステーブルの1つのレコード（1行分のデータ）を表します。

【クエリセット】
テーブルの中の複数のレコードを持った集まり、つまりデータベースから取得された複数のレコードの集合です。
クエリセットは複数のモデルオブジェクトを含んでいるため、リストのように繰り返し処理したり、個別のレコードにアクセスしたりできます。

しかし、Friend.objects.all()は、Friendインスタンスが表示される。レコード全体が表示されるのではなく、
表示されるのはクエリセット全体を簡素に文字列化したもの

ここで！
value()メソッドを使うと、レコードの値だけを(キーと値を辞書型として)取り出すことができる。
'''