from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from . import forms
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def index(request):
    reklama_list = Reklama.objects.order_by('mail')
    reklama_dict = {"reklama":reklama_list}
    return render(request,'testapp/index.html')

def loginpage(request):
    logout(request)
    username = password = ''
    if request.method == "POST":
        form = forms.LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            try:
                login(request, user)
            except Exception:
                messages.error(request, 'Ошибка входа!')
                return redirect('/login/')
            return redirect('/control/')
        else:
            messages.error(request, 'Ошибка входа!')
    else:
        form = forms.LogInForm()
    return render(request, 'testapp/controlBd/loginpage.html', {'form': form})

def signup(request):
    logout(request) # если пользователь пропишет в адресной строке url страницы регистрации, то он выйдет из уч. записи
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/control/')
        else:
            messages.error(request, 'Ошибка!')
    else:
        form = forms.SignUpForm()
    return render(request, 'testapp/controlBd/signup.html', {'form': form})

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

"""Управление Реклама"""

def reklama_control_view(request):
    list = Reklama.objects.order_by('id')
    form = forms.ReklamaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('control_reklama'))
    context = {
        'Form' : form,
        "data": list
        }
    return render(request, 'testapp/controlBd/control_reklama.html', context)

def delete_reklama(request, pk):
    print('delete')
    item = get_object_or_404(Reklama,  pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('control_reklama'))

def change_reklama(request, pk):
    print('change')
    list = Reklama.objects.order_by('id')
    item = get_object_or_404(Reklama, pk = pk)
    form = forms.ReklamaForm(request.POST or None, instance = item)
    if 'change' in request.POST:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('control_reklama'))
        context = {
            'Form' : form,
            "data": list
            }
        print('error valid')
        return render(request, 'testapp/controlBd/control_reklama_change.html', context)
    elif 'add' in request.POST:
        form = forms.ReklamaForm(request.POST or None)
        context = {
            'Form' : form,
            "data": list
            }
        return HttpResponseRedirect(reverse('control_reklama'))
    context = {
        'Form' : form,
        "data": list
        }
    return render(request, 'testapp/controlBd/control_reklama_change.html', context)

"""Управление передачи"""
def peredacha_control_view(request):
    list = Peredacha.objects.order_by('id')
    form = forms.PeredachaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('control_peredacha'))
    context = {
        'Form' : form,
        "data": list
        }
    return render(request, 'testapp/controlBd/control_peredacha.html', context)

def delete_peredacha(request, pk):
    print('delete')
    item = get_object_or_404(Peredacha,  pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('control_peredacha'))

def change_peredacha(request, pk):
    print('change')
    list = Peredacha.objects.order_by('id')
    item = get_object_or_404(Peredacha, pk = pk)
    form = forms.PeredachaForm(request.POST or None, instance = item)
    if 'change' in request.POST:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('control_peredacha'))
        context = {
            'Form' : form,
            "data": list
            }
        print('error valid')
        return render(request, 'testapp/controlBd/control_peredacha_change.html', context)
    elif 'add' in request.POST:
        form = forms.PeredachaForm(request.POST or None)
        context = {
            'Form' : form,
            "data": list
            }
        return HttpResponseRedirect(reverse('control_peredacha'))
    context = {
        'Form' : form,
        "data": list
        }
    return render(request, 'testapp/controlBd/control_peredacha_change.html', context)


# #Управление передачи
# def peredacha_control_view(request):
#     peredacha_list = Peredacha.objects.order_by('peredacha_name')
#
#     if request.method == 'POST':
#         type = None
#         if 'add' in request.POST:
#             AddPeredacha = forms.AddPeredachaForm(request.POST, prefix='Adding')
#             if AddPeredacha.is_valid():
#                 AddPeredacha.save(commit = True)
#         elif 'change' in request.POST:
#             ChangePeredacha = forms.ChangePeredachaForm(request.POST, prefix='Changing')
#             #что-то с ВАЛИДАЦИЕЙ
#             peredacha_name = request.POST.get('Changing-peredacha')
#             new_peredacha_name = request.POST.get('Changing-peredacha_name')
#             new_rek_stoim_for_min = request.POST.get('Changing-rek_stoim_for_min')
#             new_rating = request.POST.get('Changing-rating')
#             new_studiya = request.POST.get('Changing-studiya')
#             Peredacha.objects.filter(peredacha_name = peredacha_name).update(peredacha_name = new_peredacha_name)
#         elif 'delete' in request.POST:
#             DeletePeredacha = forms.DeletePeredachaForm(request.POST, prefix = 'Deleting')
#             #валидация
#             peredacha_name = request.POST.get('Deleting-reklama')
#             Reklama.objects.filter(peredacha_name = peredacha_name).delete()
#
#     return render(request, 'testapp/controlBd/control_peredacha.html', {'AddPeredachaForm': forms.AddPeredachaForm(prefix = 'Adding'), 'ChangePeredachaForm': forms.ChangePeredachaForm(prefix='Changing'), 'DeletePeredachaForm': forms.DeletePeredachaForm(prefix='Deleting'), "peredacha":peredacha_list})

"""Управление должности"""
def dolznost_control_view(request):
    list = Dolznost.objects.order_by('id')
    form = forms.DolznostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('control_dolznost'))
    context = {
        'Form' : form,
        "data": list
        }
    return render(request, 'testapp/controlBd/control_dolznost.html', context)

def delete_dolznost(request, pk):
    print('delete')
    item = get_object_or_404(Dolznost,  pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('control_dolznost'))

def change_dolznost(request, pk):
    print('change')
    list = Dolznost.objects.order_by('id')
    item = get_object_or_404(Dolznost, pk = pk)
    form = forms.DolznostForm(request.POST or None, instance = item)
    if 'change' in request.POST:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('control_dolznost'))
        context = {
            'Form' : form,
            "data": list
            }
        print('error valid')
        return render(request, 'testapp/controlBd/control_dolznost_change.html', context)
    elif 'add' in request.POST:
        form = forms.DolznostForm(request.POST or None)
        context = {
            'Form' : form,
            "data": list
            }
        return HttpResponseRedirect(reverse('control_dolznost'))
    context = {
        'Form' : form,
        "data": list
        }
    return render(request, 'testapp/controlBd/control_dolznost_change.html', context)


# """Управление должности"""
# def dolznost_control_view(request):
#     dolznost_list = Dolznost.objects.order_by('dolznost_name')
#     if request.method == 'POST':
#         if 'add' in request.POST:
#             AddDolznost = forms.AddDolznostForm(request.POST, prefix='Adding')
#             if AddDolznost.is_valid():
#                 AddDolznost.save(commit = True)
#         elif 'change' in request.POST:
#             ChangeDolznost = forms.ChangeDolznostForm(request.POST, prefix='Changing')
#             #что-то с ВАЛИДАЦИЕЙ
#             dolznost_name = request.POST.get('Changing-dolznost')
#             new_dolznost_name = request.POST.get('Changing-dolznost_name')
#             new_oklad = request.POST.get('Changing-oklad')
#             Dolznost.objects.filter(dolznost_name = dolznost_name).update(dolznost_name = new_dolznost_name)
#         elif 'delete' in request.POST:
#             DeleteDolznost = forms.DeleteDolznostForm(request.POST, prefix = 'Deleting')
#             #валидация
#             dolznost_name = request.POST.get('Deleting-dolznost')
#             Dolznost.objects.filter(dolznost_name = dolz_name).delete()
#
#     return render(request, 'testapp/controlBd/control_dolznost.html', {'AddDolznostForm': forms.AddDolznostForm(prefix = 'Adding'), 'ChangeDolznostForm': forms.ChangeDolznostForm(prefix='Changing'), 'DeleteDolznostForm': forms.DeleteDolznostForm(prefix='Deleting'), "dolznost":dolznost_list})


"""Управление сотрудники"""
def sotrudnik_control_view(request):
    sotrudnik_list = Sotrudnik.objects.order_by('id')
    form = forms.SotrudnikForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('control_sotrudnik'))
    context = {
        'SotrudnikForm' : form,
        "sotrudnik":sotrudnik_list
        }
    return render(request, 'testapp/controlBd/control_sotrudnik.html', context)

def delete_sotrudnik(request, pk):
    print('delete')
    item = get_object_or_404(Sotrudnik,  pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('control_sotrudnik'))

def change_sotrudnik(request, pk):
    print('change')
    sotrudnik_list = Sotrudnik.objects.order_by('id')
    item = get_object_or_404(Sotrudnik, pk = pk)
    form = forms.SotrudnikForm(request.POST or None, instance = item)
    if 'change' in request.POST:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('control_sotrudnik'))
        context = {
            'SotrudnikForm' : form,
            "sotrudnik":sotrudnik_list
            }
        print('error valid')
        return render(request, 'testapp/controlBd/control_sotrudnik.html', context)
    elif 'add' in request.POST:
        form = forms.SotrudnikForm(request.POST or None)
        context = {
            'SotrudnikForm' : form,
            "sotrudnik":sotrudnik_list
            }
        return HttpResponseRedirect(reverse('control_sotrudnik'))
    context = {
        'SotrudnikForm' : form,
        "sotrudnik":sotrudnik_list
        }
    return render(request, 'testapp/controlBd/control_sotrudnik_change.html', context)


"""Управление ефир"""
def efir_control_view(request):
    efir_list = Efir.objects.order_by('id')
    form = forms.EfirForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('control_efir'))
    context = {
        'EfirForm' : form,
        "efir":efir_list
        }
    return render(request, 'testapp/controlBd/control_efir.html', context)

def delete_efir(request, pk):
    print('delete')
    item = get_object_or_404(Efir,  pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('control_efir'))

def change_efir(request, pk):
    print('change')
    list = Efir.objects.order_by('id')
    item = get_object_or_404(Efir, pk = pk)
    form = forms.EfirForm(request.POST or None, instance = item)
    if 'change' in request.POST:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('control_efir'))
        context = {
            'EfirForm' : form,
            "efir": list
            }
        print('error valid')
        return render(request, 'testapp/controlBd/control_efir.html', context)
    elif 'add' in request.POST:
        form = forms.EfirForm(request.POST or None)
        context = {
            'EfirForm' : form,
            "efir": list
            }
        return HttpResponseRedirect(reverse('control_efir'))
    context = {
        'EfirForm' : form,
        "sotrudnik": list
        }
    return render(request, 'testapp/controlBd/control_efir_change.html', context)

"""Управление реклама во время ефира"""
def reklama_in_efir_control_view(request):
    list = Reklama_in_efir.objects.order_by('id')
    form = forms.Reklama_in_efirForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('control_reklama_in_efir'))
    context = {
        'Form' : form,
        "data": list
        }
    return render(request, 'testapp/controlBd/control_reklama_in_efir.html', context)

def delete_reklama_in_efir(request, pk):
    print('delete')
    item = get_object_or_404(Reklama_in_efir,  pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('control_reklama_in_efir'))

def change_reklama_in_efir(request, pk):
    print('change')
    list = Reklama_in_efir.objects.order_by('id')
    item = get_object_or_404(Efir, pk = pk)
    form = forms.Reklama_in_efirForm(request.POST or None, instance = item)
    if 'change' in request.POST:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('control_reklama_in_efir'))
        context = {
            'Form' : form,
            "data": list
            }
        print('error valid')
        return render(request, 'testapp/controlBd/control_reklama_in_efir.html', context)
    elif 'add' in request.POST:
        form = forms.Reklama_in_efirForm(request.POST or None)
        context = {
            'Form' : form,
            "data": list
            }
        return HttpResponseRedirect(reverse('control_reklama_in_efir'))
    context = {
        'Form' : form,
        "data": list
        }
    return render(request, 'testapp/controlBd/control_reklama_in_efir_change.html', context)

"""Управление сотрудник во время ефира"""
def sotrudnik_in_efir_control_view(request):
    list = Sotrudnik_in_efir.objects.order_by('id')
    form = forms.Sotrudnik_in_efirForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('control_sotrudnik_in_efir'))
    context = {
        'Form' : form,
        "data": list
        }
    return render(request, 'testapp/controlBd/control_sotrudnik_in_efir.html', context)

def delete_sotrudnik_in_efir(request, pk):
    print('delete')
    item = get_object_or_404(Sotrudnik_in_efir,  pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('control_sotrudnik_in_efir'))

def change_sotrudnik_in_efir(request, pk):
    print('change')
    list = Sotrudnik_in_efir.objects.order_by('id')
    item = get_object_or_404(Sotrudnik_in_efir, pk = pk)
    form = forms.Sotrudnik_in_efirForm(request.POST or None, instance = item)
    if 'change' in request.POST:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('control_sotrudnik_in_efir'))
        context = {
            'Form' : form,
            "data": list
            }
        print('error valid')
        return render(request, 'testapp/controlBd/sotrudnik_reklama_in_efir_change.html', context)
    elif 'add' in request.POST:
        form = forms.Sotrudnik_in_efirForm(request.POST or None)
        context = {
            'Form' : form,
            "data": list
            }
        return HttpResponseRedirect(reverse('control_sotrudnik_in_efir'))
    context = {
        'Form' : form,
        "data": list
        }
    return render(request, 'testapp/controlBd/control_reklama_in_efir_change.html', context)
