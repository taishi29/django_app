from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from .forms import SessionForm

class HelloView(TemplateView):
    
    def __init__(self):
        self.params = {
            'title' : 'Hello!',
            'form' : SessionForm(),
            'result' : None
        }
    
    def get(self, request):
        self.params['result'] = request.session.get('last_msg', 'No messaage.')
        # 辞書型のgetメソッド(辞書型.get)は、第一引数に指定されたキーに対応する値を取得するためのメソッド。もし、キーが存在しないなら、第二引数を返す。
        # 「request オブジェクトの session というセッション管理オブジェクトに対して、辞書型の get メソッドを呼び出している」
        return render(request, 'hello/index.html', self.params)    
    
    def post(self, request):
        ses = request.POST['session']
        self.params['result'] = 'send: "' + ses + '".'
        request.session['last_msg'] = ses
        self.params['form'] = SessionForm(request.POST)
        return render(request, 'hello/index.html', self.params)
        

