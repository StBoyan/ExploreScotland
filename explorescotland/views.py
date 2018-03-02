from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'explorescotland/home.html', {})

def about(request):
    return render(request, 'explorescotland/about.html', {})

@login_required
def parent_area(request):
    return render(request, 'explorescotland/parent_area.html', {})

def parentlogin(request):
    return render(request,'explorescotland/parentlogin.html',{})

def userHomePage (request):
    return render(request, 'explorescotland/userHomePage.html', {})

def scot (request):
    return render(request, 'explorescotland/personaScot.html', {})

def lily (request):
    return render(request, 'explorescotland/personaLily.html', {})
def googlemap(request):
    return render(request,'explorescotland/googlemap.html',{})

