"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from testapp import views

urlpatterns = [
    path(r'',views.index, name = 'index'),
    url(r'^testapp/',include('testapp.urls')),
    path('admin/', admin.site.urls),
    path('control/', views.control_view, name = 'control_main'),
    path('control/reklama/', views.reklama_control_view, name = 'control_reklama'),
    path('control/dolznost/', views.dolznost_control_view, name = 'control_dolznost'),
    path('control/sotrudnik/', views.sotrudnik_control_view, name = 'control_sotrudnik'),
    path('control/sotrudnik/<int:pk>/delete', views.delete_sotrudnik, name='delete_sotrudnik'),
    path('control/sotrudnik/<int:pk>/change', views.change_sotrudnik, name='change_sotrudnik'),
    path('control/efir/', views.efir_control_view, name = 'control_efir'),
    path('control/efir/<int:pk>/delete', views.delete_efir, name='delete_efir'),
    path('control/efir/<int:pk>/change', views.change_efir, name='change_efir'),
    path('control/reklama_in_efirir/', views.reklama_in_efir_control_view, name = 'control_reklama_in_efir'),
    path('control/reklama_in_efirir/<int:pk>/delete', views.delete_reklama_in_efir, name='delete_reklama_in_efir'),
    path('control/reklama_in_efirir/<int:pk>/change', views.change_reklama_in_efir, name='change_reklama_in_efir'),
    path('control/sotrudnik_in_efirir/', views.sotrudnik_in_efir_control_view, name = 'control_sotrudnik_in_efir'),
    path('control/sotrudnik_in_efirir/<int:pk>/delete', views.delete_sotrudnik_in_efir, name='delete_sotrudnik_in_efir'),
    path('control/sotrudnik_in_efirir/<int:pk>/change', views.change_sotrudnik_in_efir, name='change_sotrudnik_in_efir'),
    path('control/dolznost/', views.dolznost_control_view, name = 'control_dolznost'),
    path('control/dolznost/<int:pk>/delete', views.delete_dolznost, name='delete_dolznost'),
    path('control/dolznost/<int:pk>/change', views.change_dolznost, name='change_dolznost'),
    path('control/peredacha/', views.peredacha_control_view, name = 'control_peredacha'),
    path('control/peredacha/<int:pk>/delete', views.delete_peredacha, name='delete_peredacha'),
    path('control/peredacha/<int:pk>/change', views.change_peredacha, name='change_peredacha'),
]
