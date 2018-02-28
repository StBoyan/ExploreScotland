from django.shortcuts import render

def home(request):
    return render(request, 'explorescotland/home.html', {})
