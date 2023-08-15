from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

def Formulario(request):
    return render (request, 'Login.js', {
        'formu': UserCreationForm
    })