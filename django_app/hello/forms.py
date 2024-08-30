from django import forms

class HelloForm(forms.Form):
    data = [
        ('season 1', '賢者の石'),
        ('season 2', '秘密の部屋'),
        ('season 3', 'アズカバンの囚人')
    ] 
    choice = forms.MultipleChoiceField(label='radio', choices=data, widget=forms.SelectMultiple(attrs={'size':3, 'class':'form-select'}))
    
