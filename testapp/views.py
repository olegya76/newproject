from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from . import forms

# Create your views here.

# Our original index view function
# Corresponds to original_index.html (rename it to index.html to use it!)

# def index(request):
#     my_dict = {'insert_me':"Now I am coming from first_app/index.html!"}
#     # Make sure this is pointing to the correct index
#     return render(request,'first_app/index.html',context=my_dict)


def index(request):
    reklama_list = Reklama.objects.order_by('mail')
    reklama_dict = {"reklama":reklama_list}
    return render(request,'testapp/index.html')

def reklama(request):
    reklama_list = Reklama.objects.order_by('mail')
    reklama_dict = {"reklama":reklama_list}
    return render(request, 'testapp/reklama.html', context = reklama_dict)

def form_reklama_view(request):
    form = forms.FormReklama()

    # Check to see if we get a POST back.
    if request.method == 'POST':
        # In which case we pass in that request.
        form = forms.FormReklama(request.POST)

        # Check to see form is valid
        if form.is_valid():
            # Do something.
            print("Form Validation Success. Prints in console.")
            print("Name"+form.cleaned_data['name'])
            print("Email"+form.cleaned_data['rekvesit'])
            print('Text'+form.cleaned_data['mail'])
    return render(request,'testapp/form_reklama.html',{'form':form})

def new_reklama_view(request):
    form = forms.NewReklamaForm
    if request.method == 'POST':
        form = forms.NewReklamaForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return reklama(request)
        else:
            print('ERROR FORM INVALID')
    else:
        return render(request, 'testapp/new_reklama.html', {'form':form})

def control_view(request):
    return render(request, 'testapp/controlBd/main.html')

#Управление Реклама
def reklama_control_view(request):
    reklama_list = Reklama.objects.order_by('mail')
    reklama_dict = {"reklama":reklama_list}
    if request.method == 'POST':
        type = None
        if 'add' in request.POST:
            AddReklama = forms.AddReklamaForm(request.POST, prefix='Adding')
            if AddReklama.is_valid():
                AddReklama.save(commit = True)
        elif 'change' in request.POST:
            ChangeReklama = forms.ChangeReklamaForm(request.POST, prefix='Changing')
            #что-то с ВАЛИДАЦИЕЙ
            reklama_name = request.POST.get('Changing-reklama')
            new_reklama_name = request.POST.get('Changing-reklama_name')
            new_rekvesit = request.POST.get('Changing-rekvesit')
            new_mail = request.POST.get('Changing-mail')
            print('reklama_name', reklama_name, 'new_reklama_name', new_reklama_name)
            Reklama.objects.filter(reklama_name = reklama_name).update(reklama_name = new_reklama_name)
        elif 'delete' in request.POST:
            DeleteReklama = forms.DeleteReklamaForm(request.POST, prefix = 'Deleting')
            #валидация
            reklama_name = request.POST.get('Deleting-reklama')
            Reklama.objects.filter(reklama_name = reklama_name).delete()

    return render(request, 'testapp/controlBd/control_reklama.html', {'AddReklamaForm': forms.AddReklamaForm(prefix = 'Adding'), 'ChangeReklamaForm': forms.ChangeReklamaForm(prefix='Changing'), 'DeleteReklamaForm': forms.DeleteReklamaForm(prefix='Deleting'), "reklama":reklama_list})


#Управление передачи
def peredacha_control_view(request):
    peredacha_list = Peredacha.objects.order_by('peredacha_name')

    if request.method == 'POST':
        type = None
        if 'add' in request.POST:
            AddPeredacha = forms.AddPeredachaForm(request.POST, prefix='Adding')
            if AddPeredacha.is_valid():
                AddPeredacha.save(commit = True)
        elif 'change' in request.POST:
            ChangePeredacha = forms.ChangePeredachaForm(request.POST, prefix='Changing')
            #что-то с ВАЛИДАЦИЕЙ
            peredacha_name = request.POST.get('Changing-peredacha')
            new_peredacha_name = request.POST.get('Changing-peredacha_name')
            new_rek_stoim_for_min = request.POST.get('Changing-rek_stoim_for_min')
            new_rating = request.POST.get('Changing-rating')
            new_studiya = request.POST.get('Changing-studiya')
            Peredacha.objects.filter(peredacha_name = peredacha_name).update(peredacha_name = new_peredacha_name)
        elif 'delete' in request.POST:
            DeletePeredacha = forms.DeletePeredachaForm(request.POST, prefix = 'Deleting')
            #валидация
            peredacha_name = request.POST.get('Deleting-reklama')
            Reklama.objects.filter(peredacha_name = peredacha_name).delete()

    return render(request, 'testapp/controlBd/control_peredacha.html', {'AddPeredachaForm': forms.AddPeredachaForm(prefix = 'Adding'), 'ChangePeredachaForm': forms.ChangePeredachaForm(prefix='Changing'), 'DeletePeredachaForm': forms.DeletePeredachaForm(prefix='Deleting'), "peredacha":peredacha_list})


#Управление должности
def dolznost_control_view(request):
    dolznost_list = Dolznost.objects.order_by('dolznost_name')

    if request.method == 'POST':
        type = None
        if 'add' in request.POST:
            AddDolznost = forms.AddDolznostForm(request.POST, prefix='Adding')
            if AddDolznost.is_valid():
                AddDolznost.save(commit = True)
        elif 'change' in request.POST:
            ChangeDolznost = forms.ChangeDolznostForm(request.POST, prefix='Changing')
            #что-то с ВАЛИДАЦИЕЙ
            dolznost_name = request.POST.get('Changing-dolznost')
            new_dolznost_name = request.POST.get('Changing-dolznost_name')
            new_oklad = request.POST.get('Changing-oklad')
            Dolznost.objects.filter(dolznost_name = dolznost_name).update(dolznost_name = new_dolznost_name)
        elif 'delete' in request.POST:
            DeleteDolznost = forms.DeleteDolznostForm(request.POST, prefix = 'Deleting')
            #валидация
            dolznost_name = request.POST.get('Deleting-dolznost')
            Dolznost.objects.filter(dolznost_name = dolz_name).delete()

    return render(request, 'testapp/controlBd/control_dolznost.html', {'AddDolznostForm': forms.AddDolznostForm(prefix = 'Adding'), 'ChangeDolznostForm': forms.ChangeDolznostForm(prefix='Changing'), 'DeleteDolznostForm': forms.DeleteDolznostForm(prefix='Deleting'), "dolznost":dolznost_list})


#Управление ссотрудники
def sotrudnik_control_view(request):
    sotrudnik_list = Sotrudnik.objects.order_by('id')

    if request.method == 'POST':
        type = None
        if 'add' in request.POST:
            AddSotrudnik = forms.AddSotrudnikForm(request.POST, prefix='Adding')
            if AddSotrudnik.is_valid():
                change_sotrudnik = AddSotrudnik.save(commit = False)
                change_sotrudnik.id_dolznost = request.POST.get('Adding-dolznost')
                change_sotrudnik.save()
                print(request.POST.get('Adding-dolznost'))
                print(change_sotrudnik)
                AddSotrudnik.save_m2m()
            else :
                print('error valid')
        # elif 'change' in request.POST:
        #     ChangeSotrudnik = forms.ChangeSotrudnikForm(request.POST, prefix='Changing')
        #     #что-то с ВАЛИДАЦИЕЙ
        #     id_sotrudnik_name = request.POST.get('Changing-sotrudnik_id')
        #     new_sotrudnik_name = request.POST.get('Changing-name')
        #     new_oklad = request.POST.get('Changing-oklad')
        #     Dolznost.objects.filter(dolznost_name = dolznost_name).update(dolznost_name = new_dolznost_name)
        # elif 'delete' in request.POST:
        #     DeleteDolznost = forms.DeleteDolznostForm(request.POST, prefix = 'Deleting')
        #     #валидация
        #     dolznost_name = request.POST.get('Deleting-dolznost')
        #     Dolznost.objects.filter(dolznost_name = dolz_name).delete()

    return render(request, 'testapp/controlBd/control_sotrudnik.html', {'AddSotrudnikForm': forms.AddSotrudnikForm(prefix = 'Adding'), 'ChangeSotrudnikForm': forms.ChangeSotrudnikForm(prefix='Changing'), 'DeleteSotrudnikForm': forms.DeleteSotrudnikForm(prefix='Deleting'), "sotrudnik":sotrudnik_list})
