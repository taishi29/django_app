from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:page>', views.index, name='index'),
    path('post', views.post, name='post'),
    path('goods', views.goods, name='goods'),
    path('good/<int:good_id>', views.good, name='good'),
]
