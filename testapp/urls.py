from django.conf.urls import url
from django.urls import path
from testapp import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    path('reklama/', views.reklama, name = 'reklama'),
    path('new_reklama/', views.new_reklama_view, name = 'new_reklama')
]
