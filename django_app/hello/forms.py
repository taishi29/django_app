from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(label='Name', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    mail = forms.EmailField(label='Email', \
        widget=forms.EmailInput(attrs={'class':'form-control'}))
    gender = forms.BooleanField(label='Gender', required=False, \
        widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    age = forms.IntegerField(label='Age', \
        widget=forms.NumberInput(attrs={'class':'form-control'}))
    birthday = forms.DateField(label='Birth', \
        widget=forms.DateInput(attrs={'class':'form-control'}))

"""    
【CharField】
ユーザーにテキストを入力させるためのフォームフィールドを作成する。テキストボックスとしてHTMLにレンダリングされる。
【widget】
フィールドがどのように表示されるかを指定するもの。widget=forms.TextInputとすることで、CharFieldがテキスト入力フィールド
<input type="text">としてレンダリングされるようになる(そもそも、CharField自体、デフォルトでそうなっているが)。widgetを指定することで、フィールドのHTMLタグの形や属性をカスタマイズすることができる。
【attrs】
ウィジェットに対して追加のHTML属性を指定するための辞書型の引数。
例えば、class属性を設定してCSSスタイルを適用したり、placeholder属性を設定して入力フィールドにヒントテキストを表示することができる。
"""
