from django import forms
from.models import Friend

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']
        
'''
ModelFormとは、Djangoにおいてモデル（Model）に基づいたフォームを自動的に生成するためのクラスです。
DjangoのModelFormを使用することで、データベースモデルのフィールドに対応したフォームを簡単に作成し、
データのバリデーションや保存をモデルと自動的にリンクさせることができます。
'''