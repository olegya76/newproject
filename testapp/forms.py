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
#Добавление рекламы
class AddReklamaForm(forms.ModelForm):
    class Meta():
        model = models.Reklama
        fields = '__all__'
        labels = {
            'reklama_name': 'Название компании',
            'rekvesit': 'Реквезиты',
            'mail': 'Email компании',
        }
#Изменение рекламы
class ChangeReklamaForm(forms.ModelForm):
    reklama = forms.ModelChoiceField(queryset=models.Reklama.objects.values_list('reklama_name', flat=True), empty_label=None, label='Выберите рекомодателя')
    class Meta():
        model = models.Reklama
        fields = '__all__'
        labels = {
            'reklama_name': 'Название компании',
            'rekvesit': 'Реквезиты',
            'mail': 'Email компании',
        }
#Удаление рекламы
class DeleteReklamaForm(forms.Form):
    reklama = forms.ModelChoiceField(queryset=models.Reklama.objects.values_list('reklama_name', flat=True), empty_label=None, label='Выберите рекомодателя')


"""Управление: Передача"""
#Добавление передачи
class AddPeredachaForm(forms.ModelForm):
    class Meta():
        model = models.Peredacha
        fields = '__all__'
        labels = {
            'peredacha_name': 'Название передачи',
            'rek_stoim_for_min': 'Стоимость рекламы за 1 минуту',
            'rating': 'Рейтинг передачи',
            'studiya': 'Студия'
        }
#Изменение передачи
class ChangePeredachaForm(forms.ModelForm):
    peredacha = forms.ModelChoiceField(queryset=models.Peredacha.objects.values_list('peredacha_name', flat=True), empty_label=None, label='Выберите передачу')
    class Meta():
        model = models.Peredacha
        fields = '__all__'
        labels = {
            'peredacha_name': 'Название передачи',
            'rek_stoim_for_min': 'Стоимость рекламы за 1 минуту',
            'rating': 'Рейтинг передачи',
            'studiya': 'Студия'
        }
#Удаление передачи
class DeletePeredachaForm(forms.Form):
    peredacha = forms.ModelChoiceField(queryset=models.Peredacha.objects.values_list('peredacha_name', flat=True), empty_label=None, label='Выберите передачу')

"""Управление: Должность"""
#Добавление должности
class AddDolznostForm(forms.ModelForm):
    class Meta():
        model = models.Dolznost
        fields = '__all__'
        labels = {
            'dolznost_name': 'Название должности',
            'oklad': 'Оклад сотрудника на этой должности',
        }
#Изменение должности
class ChangeDolznostForm(forms.ModelForm):
    dolznost = forms.ModelChoiceField(queryset=models.Dolznost.objects.values_list('dolznost_name', flat=True), empty_label=None, label='Выберите должность')
    class Meta():
        model = models.Dolznost
        fields = '__all__'
        labels = {
            'dolznost_name': 'Название должности',
            'oklad': 'Оклад сотрудника на этой должности',
        }
#Удаление должности
class DeleteDolznostForm(forms.Form):
    dolznost = forms.ModelChoiceField(queryset=models.Dolznost.objects.values_list('dolznost_name', flat=True), empty_label=None, label='Выберите должность')

"""Управление: Сотрудник"""
#Добавление сотрудника
class AddSotrudnikForm(forms.ModelForm):
    dolznost = forms.ModelChoiceField(queryset=models.Dolznost.objects.values_list('dolznost_name', flat=True), empty_label=None, label='Выберите должность')
    class Meta():
        model = models.Sotrudnik
        fields = '__all__'
        exclude = ['id_dolznost']
        labels = {
            'fam': 'Фамилия',
            'name': 'Имя',
            'otchestvo': 'Отчество',
            'kard_number': 'Номер карты',
            'otdel': 'Отдел',
            'passport_number': 'Паспорт',
            'data_priom': 'Дата приема на работу',
        }
#Изменение должности
class ChangeSotrudnikForm(forms.ModelForm):
    sotrudnik_id = forms.ModelChoiceField(queryset=models.Sotrudnik.objects.values_list('id', flat=True), empty_label=None, label='Выберите id сотрудника')
    sotrudnik_fam = forms.ModelChoiceField(queryset=models.Sotrudnik.objects.values_list('fam', flat=True), empty_label=None, label='Выберите фамилию сотрудника')
    sotrudnik_name = forms.ModelChoiceField(queryset=models.Sotrudnik.objects.values_list('name', flat=True), empty_label=None, label='Выберите Имя сотрудника')
    dolznost = forms.ModelChoiceField(queryset=models.Dolznost.objects.values_list('dolznost_name', flat=True), empty_label=None, label='Выберите должность')
    class Meta():
        model = models.Sotrudnik
        fields = '__all__'
        exclude = ['id_dolznost']
        labels = {
            'fam': 'Фамилия',
            'name': 'Имя',
            'otchestvo': 'Отчество',
            'kard_number': 'Номер карты',
            'otdel': 'Отдел',
            'passport_number': 'Паспорт',
            'data_priom': 'Дата приема на работу',
        }
#Удаление должности
class DeleteSotrudnikForm(forms.Form):
    sotrudnik_fam = forms.ModelChoiceField(queryset=models.Sotrudnik.objects.values_list('fam', flat=True), empty_label=None, label='Выберите фамилию сотрудника')
    sotrudnik_name = forms.ModelChoiceField(queryset=models.Sotrudnik.objects.values_list('name', flat=True), empty_label=None, label='Выберите Имя сотрудника')


#Новая передача
class NewPeredachaForm(forms.ModelForm):
    class Meta():
        model = models.Peredacha
        fields = '__all__'

#Новая должность
class NewDolznostForm(forms.ModelForm):
    class Meta():
        model = models.Dolznost
        fields = '__all__'

#Новый сотрудник
class NewSotrudnikForm(forms.ModelForm):
    class Meta():
        model = models.Sotrudnik
        fields = '__all__'

class NewEfirForm(forms.ModelForm):
    class Meta():
        model = models.Efir
        fields = '__all__'

class NewSotrudnikInEfirForm(forms.ModelForm):
    class Meta():
        model = models.Sotrudnik_in_efir
        fields = '__all__'

class NewReklamaInEfirForm(forms.ModelForm):
    class Meta():
        model = models.Reklama_in_efir
        fields = '__all__'
