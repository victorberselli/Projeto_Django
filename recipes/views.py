from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def Home(request):  
    return HttpResponse(f'HOME_1'.upper())

def Contato(request):
    return HttpResponse(f'CONTATO'.upper())

def Sobre(request):
    return HttpResponse(f'SOBRE'.upper())