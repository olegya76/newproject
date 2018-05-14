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
