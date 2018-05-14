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
