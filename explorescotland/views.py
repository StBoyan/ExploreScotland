from django.shortcuts import render
from django.core.urlresolvers import reverse

def home(request):
    return render(request, 'explorescotland/home.html', {})

def parentlogin(request):
    return render(request,'explorescotland/parentlogin.html',{})
    
def userHomePage (request):
    return render(request, 'explorescotland/userHomePage.html', {})

def scot (request):
    return render(request, 'explorescotland/personaScot.html', {})

def lily (request):
    return render(request, 'explorescotland/personaLily.html', {})
