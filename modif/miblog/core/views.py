from django.shortcuts import render

from django.conf import settings




def home(request):
    return render(request,'core/home.html')

def tienda(request):
    return render(request,'core/tienda.html')

def skins(request):
    return render(request,'core/skins.html')













