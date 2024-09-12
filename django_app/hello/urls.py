from django.urls import path
from . import views
from .views import FriendList
from .views import FriendDetail

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('list', FriendList.as_view()),
    path('detail/<int:pk>', FriendDetail.as_view()),
]

'''
as_view() を呼び出すと、Djangoがクラスを関数のように扱えるように変換します。
FriendListView.as_view()を使うことで、Djangoは「GETリクエストが来たらどのメソッドを実行するか」や「POSTリクエストが来たらどうするか」といった動作を自動で処理してくれます。

まとめると：
URLパターン：http://localhost:8000/hello/list にアクセスすると、
ビュー：FriendList クラスが呼び出され、
データ：Friend モデルの全データを取得して、
テンプレート：friend_list.html が自動的に表示されます。
'''
