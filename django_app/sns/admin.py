from django.contrib import admin
from .models import Message, Good

admin.site.register(Message)
admin.site.register(Good)
# Register your models here.

'''
Django Adminとは？
Django Adminは、Djangoが標準で提供する強力な管理画面で、データベースに保存されているデータをウェブインターフェースを通じて操作できるシステムである。
管理者ユーザーとしてログインすると、登録されたすべてのモデルにアクセスでき、以下のような操作が可能になる。
'''