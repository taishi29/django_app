from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.forms.models import model_to_dict

from .models import Message2, Good2

import json

page_max = 10

# indexのビュー関数
@login_required(login_url='/admin/login/')
def index(request):
    return render(request, 'index.html')

# メッセージをJSONで送信する
@login_required(login_url='/admin/login/')
def msgs(request, page=1):
    msgs = Message2.objects.all()
    # ページネーションで指定ページを取得
    paginate = Paginator(msgs, page_max)
    page_items = paginate.get_page(page)
    serialized_data = serialize('json', page_items)
    return HttpResponse(serialized_data, content_type='application/json')

# ページ数を返す
@login_required(login_url='/admin/login/')
def plast(request):
    msgs = Message2.objects.all()
    # ページネーションで指定ページを取得
    paginate = Paginator(msgs, page_max)
    last_page = paginate.num_pages
    return JsonResponse({'result':"OK", 'value':last_page})

# ユーザー名を返す
@login_required(login_url='/admin/login/')
def usr(request, usr_id=-1):
    if usr_id == -1:
        usr = request.user
    else:
        usr = User.objects.filter(id=usr_id).first()
    return JsonResponse({'result': "OK", 'value': usr.username})

# メッセージのポスト処理
@login_required(login_url='/admin/login/')
def post(request):
    # POST送信の処理
    if request.method == 'POST':
        # 送信内容の取得
        byte_data = request.body.decode('utf-8')
        json_body = json.loads(byte_data)

        # Messageを作成し設定して保存
        msg = Message2()
        msg.owner = request.user
        msg.owner_name = request.user.username
        msg.content = json_body['content']
        msg.save()
        return HttpResponse("OK")    
    else:
        return HttpResponse("NG")    
    
# goodボタンの処理
@login_required(login_url='/admin/login/')
def good(request, good_id):
    # goodするMessageを取得
    good_msg = Message2.objects.get(id=good_id)
    # 自分がメッセージにGoodした数を調べる
    is_good = Good2.objects.filter(owner=request.user).filter(message=good_msg).count()
    # ゼロより大きければすでにgood済み
    if is_good > 0:
        return HttpResponse("NG")    
    
    else:
        # Messageのgood_countを１増やす
        good_msg.good_count += 1
        good_msg.save()
        # Goodを作成し、設定して保存
        good = Good2()
        good.owner = request.user
        good.message = good_msg
        good.save()
        return HttpResponse("OK")    
