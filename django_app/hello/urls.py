from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
]

'''
・<int:num> は、DjangoのURLパターンにおけるパスコンバーターです。
・これは、URLの一部を整数としてキャプチャし、その値を num という引数としてビュー関数に渡します。
・この書き方はDjango独自のものであり、Python標準の文法ではありません。
・Djangoには他にもstr、slug、uuid、pathなどのパスコンバーターがあります。
このように、DjangoのURLパターンでパスコンバーターを使うと、URL内の動的な部分（数値や文字列など）をビューに渡して処理することが簡単にできます。
'''
