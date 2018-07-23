from django import forms
from django.core import validators
from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username', 'password1', 'password2')

"""Форма авторизации"""
class LogInForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)

"""Управление: Реклама"""
class ReklamaForm(forms.ModelForm):
    class Meta():
        model = models.Reklama
        fields = '__all__'
        labels = {
            'reklama_name': 'Название компании',
            'rekvesit': 'Реквезиты',
            'mail': 'Email компании',
        }

"""Управление: Передача"""
class PeredachaForm(forms.ModelForm):
    class Meta():
        model = models.Peredacha
        fields = '__all__'
        labels = {
            'peredacha_name': 'Название передачи',
            'rek_stoim_for_min': 'Стоимость рекламы за 1 минуту',
            'rating': 'Рейтинг передачи',
            'studiya': 'Студия'
        }

"""Управление: Должность"""
class DolznostForm(forms.ModelForm):
    class Meta():
        model = models.Dolznost
        fields = '__all__'
        labels = {
            'dolznost_name': 'Название должности',
            'oklad': 'Оклад сотрудника на этой должности',
        }

"""Управление: Сотрудник"""
class SotrudnikForm(forms.ModelForm):
    id_dolznost = forms.ModelChoiceField(
    queryset=models.Dolznost.objects.all(), empty_label=None,
    label='Выберите должность')
    class Meta():
        model = models.Sotrudnik
        fields = '__all__'
        labels = {
            'fam': 'Фамилия',
            'name': 'Имя',
            'otchestvo': 'Отчество',
            'kard_number': 'Номер карты',
            'otdel': 'Отдел',
            'passport_number': 'Паспорт',
            'data_priom': 'Дата приема на работу',
        }

"""Управление: Сотрудник"""
class SearchSotrudnikForm(forms.ModelForm):
    id_dolznost = forms.ModelChoiceField(
    queryset=models.Dolznost.objects.all(), empty_label="",
    label='Выберите должность', required = False)
    fam = forms.CharField(
    label='Фамилия', required = False)
    name = forms.CharField(
    label='Имя', required = False)
    otchestvo = forms.CharField(
    label='Отчество', required = False)
    kard_number = forms.CharField(
    label='Номер карты', required = False)
    otdel = forms.IntegerField(
    label='Отдел', required = False)
    #initial = 1
    passport_number = forms.CharField(
    label='Номер паспорта', required = False)
    data_priom = forms.DateField(
    label='Дата приема на работу', required = False)
    class Meta:
        model = models.Sotrudnik
        fields = '__all__'
        labels = {
            'fam': 'Фамилия',
            'name': 'Имя',
            'otchestvo': 'Отчество',
            'kard_number': 'Номер карты',
            'otdel': 'Отдел',
            'passport_number': 'Паспорт',
            'data_priom': 'Дата приема на работу',
        }

"""Управление Ефир"""
class EfirForm(forms.ModelForm):
    id_peredacha = forms.ModelChoiceField(
    queryset = models.Peredacha.objects.all(), empty_label = None,
    label = 'Выберете передачу'
    )
    class Meta():
        model = models.Efir
        fields = '__all__'
        labels = {
        'start_efir': 'Начало ефира',
        'stop_efir': 'Окончание ефира',
        }

"""Управление Реклама в ефире"""
class Reklama_in_efirForm(forms.ModelForm):
    id_reklama = forms.ModelChoiceField(
    queryset = models.Reklama.objects.all(), empty_label = None,
    label = 'Выберете рекламу'
    )
    id_efir = forms.ModelChoiceField(
    queryset = models.Efir.objects.all(), empty_label = None,
    label = 'Выберете ефир'
    )
    class Meta():
        model = models.Reklama_in_efir
        fields = '__all__'

"""Управление Сотрудник в ефире"""
class Sotrudnik_in_efirForm(forms.ModelForm):
    id_sotrudnik = forms.ModelChoiceField(
    queryset = models.Sotrudnik.objects.all(), empty_label = None,
    label = 'Выберете сотрудника'
    )
    id_efir = forms.ModelChoiceField(
    queryset = models.Efir.objects.all(), empty_label = None,
    label = 'Выберете ефир'
    )
    class Meta():
        model = models.Sotrudnik_in_efir
        fields = '__all__'
