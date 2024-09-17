from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('plast', views.plast, name='plast'),
    path('msgs/<int:page>', views.msgs, name='msgs'),
    path('usr', views.usr, name='usr'),
    path('usr/<int:usr_id>', views.usr, name='usr'),
    path('post', views.post, name='post'),
    path('good/<int:good_id>', views.good, name='good'),
]
