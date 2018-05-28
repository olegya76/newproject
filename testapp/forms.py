from django import forms
from django.core import validators
from . import models

# Very Basic Example of a Django Form

class FormReklama(forms.Form):
    name = forms.CharField()
    rekvesit = forms.CharField()
    mail = forms.EmailField()
    # test = forms.CharField(label = 'sdfsdf')

    # def clean(self):
    #     all_clean_data = super().clean()
    #     fmail = all_clean_data['mail']
    #     vmail = all_clean_data['test']
    #     if fmail != vmail:
    #         raise forms.ValidationError("NOT MATCH")

class NewReklamaForm(forms.ModelForm):
    class Meta():
        model = models.Reklama
        fields = '__all__'
        help_texts = {
            'reklama_name': 'Название компании',
            'rekvesit': 'Реквезиты',              # не работает почему-то     | в документации
            'mail': 'Email компании help',  # и это                     | такого нет
        }
        labels = {
            'reklama_name': 'Название компании',
            'rekvesit': 'Реквезиты',
            'mail': 'Email компании labels',
        }
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
