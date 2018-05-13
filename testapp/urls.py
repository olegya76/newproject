from django.conf.urls import url
from django.urls import path
from testapp import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    path('reklama/', views.reklama, name = 'reklama')
]
