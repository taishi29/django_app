from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required


from .models import Message, Good
from .forms import PostForm

# indexのビュー関数
@login_required(login_url='/admin/login/')
def inde(request, page=1):
    max = 10
    form = PostForm(request.user)
    msgs = Message.objects.all()
    # ページネーションで指定ページを取得
    paginate = Paginator(msgs, max)
    page_items = paginate.get_page(page)
    
    params = {
       'login_user':request.user,
       'form': form,
       'contents':page_items,
    }
    return render(request, 'sns/index.html', params)

# goodsのビュー関数
@login_required(login_url='admin/login/')
def goods(request):
    goods = Good.objects.filter(owner=request.user).all()
    
    params = {
        'login_user':request.user,
        'contents':goods,
    }
    return render(request, 'sns/good.html', params)

# メッセージのポスト処理
@login_required(login_url='/admin/login/')
def post(request):
    # POST送信の処理
    if request.method == 'POST':
        # 送信内容の取得
        content = request.POST['content']
        # Messageを作成し設定して保存
        msg = Message()
        msg.owner = request.user
        msg.content = content
        msg.save()
        return redirect(to='/sns/')
    
    else:
        message = Message.objects.filter(owner=request.user).all()
        params = {
            'login_user':request.user,
            'contents':messages,
        }
        return render(request, 'sns/post.html', params)
    
# goodボタンの処理
@login_required(login_url='/admin/login/')
def good(request, good_id):
    # goodするMessageを取得
    good_msg = Message.objects.get(id=good_id)
    # 自分がメッセージにGoodした数を調べる
    is_good = Good.objects.filter(owner=request.user).filter(message=good_msg).count()
    # ゼロより大きければすでにgood済み
    if is_good > 0:
        messages.success(request, 'すでにメッセージにはGoodしています。')
        return redirect(to='/sns')
    
    # Messageのgood_countを１増やす
    good_msg.good_count += 1
    good_msg.save()
    # Goodを作成し、設定して保存
    good = Good()
    good.owner = request.user
    good.message = good_msg
    good.save()
    # メッセージを設定
    messages.success(request, 'メッセージにGoodしました!')
    return redirect(to='/sns')
# Create your views here.
