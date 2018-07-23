from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from . import forms
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

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

"""Страница управления данными"""
@login_required
def control_view(request):
    #print(user.username)
    return render(request, 'testapp/controlBd/main.html')

"""Управление Реклама"""
def reklama_control_view(request):
    list = Reklama.objects.order_by('id')
    print(list)
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


"""Поиск сотрудника"""
def search_sotrudnik(request):
    if request.method == 'POST':
        fam = request.POST.get('fam')
        name = request.POST.get('name')
        otchestvo = request.POST.get('otchestvo')
        kard_number = request.POST.get('kard_number')
        if request.POST.get('otdel'):
            otdel = request.POST.get('otdel')
        else:
            otdel = -1
        passport_number = request.POST.get('passport_number')
        if request.POST.get('id_dolznost'):
            id_dolznost = request.POST.get('id_dolznost')
        else:
            id_dolznost = -1
        if request.POST.get('data_priom'):
            data_priom = request.POST.get('data_priom')
        else:
            data_priom = "0001-01-01"
        print(fam)
        form = forms.SearchSotrudnikForm(request.POST or None)
        list = Sotrudnik.objects.filter(
        Q(fam = fam)
        | Q(name = name)
        | Q(otchestvo = otchestvo)
        | Q(kard_number = kard_number)
        | Q(otdel = otdel)
        | Q(passport_number = passport_number)
        | Q(id_dolznost = id_dolznost)
        | Q(data_priom = data_priom)
        )
        context = {
            'Form' : form,
            "data": list
            }
        return render(request, 'testapp/search_sotrudnik.html', context)
    form = forms.SearchSotrudnikForm(request.POST or None)
    list = Sotrudnik.objects.order_by('id')
    context = {
        'Form' : form,
        "data": list
        }
    return render(request, 'testapp/search_sotrudnik.html', context)


"""Поиск сотрудника во время ефиров"""
def search_efir_in_sotrudnik(request):
    if request.method == 'POST':
        sotrudnik = request.POST.get('id_sotrudnik')
        print(sotrudnik)
        form = forms.Sotrudnik_in_efirForm(request.POST or None)
        list = Sotrudnik_in_efir.objects.filter( Q(id_sotrudnik = sotrudnik) )
        context = {
            'Form' : form,
            "data": list
            }
        return render(request, 'testapp/search_efir_in_sotrudnik.html', context)
    form = forms.Sotrudnik_in_efirForm(request.POST or None)
    list = Sotrudnik_in_efir.objects.order_by('id')
    context = {
        'Form' : form,
        "data": list
        }
    return render(request, 'testapp/search_efir_in_sotrudnik.html', context)


"""Поиск сотрудников назначеных на ефир"""
def search_sotrudnik_in_efir(request):
    if request.method == 'POST':
        efir = request.POST.get('id_efir')
        print(efir)
        form = forms.Sotrudnik_in_efirForm(request.POST or None)
        list = Sotrudnik_in_efir.objects.filter( Q(id_efir = efir) )
        context = {
            'Form' : form,
            "data": list
            }
        return render(request, 'testapp/search_sotrudnik_in_efir.html', context)
    form = forms.Sotrudnik_in_efirForm(request.POST or None)
    list = Sotrudnik_in_efir.objects.order_by('id')
    context = {
        'Form' : form,
        "data": list
        }
    return render(request, 'testapp/search_sotrudnik_in_efir.html', context)
