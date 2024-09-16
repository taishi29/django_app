from django import forms
from.models import Message, Good
from django.contrib.auth.models import User

# Messageのフォーム
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['owner', 'content']

# Goodのフォーム
class Good(forms.ModelForm):
    class Meta:
        model = Good
        fields = ['owner', 'message']

# 投稿フォーム
class PostForm(forms.Form):
    content = forms.CharField(max_length=500, \
        widget=forms.Textarea(attrs={'class':'form-control', 'rows':2}))
    
    def __init__(self, user, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)