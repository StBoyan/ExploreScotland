from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from explorescotland.forms import FeedbackForm, ProfileForm
from explorescotland.models import Feedback
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'explorescotland/home.html', {})

def about(request):
    return render(request, 'explorescotland/about.html', {})

@login_required
def parent_area(request):
    return render(request, 'explorescotland/parent_area.html', {})

@login_required
def feedback(request):
    form = FeedbackForm()

    if request.method == 'POST':
        # Links current user to the feedback
        feedback = Feedback(parent=request.user)
        form = FeedbackForm(request.POST, instance=feedback)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('parent_area')) #Can make this redirect to a thank you page
        else:
            print(form.errors)

    return render(request, 'explorescotland/feedback.html', {'form': form})

@login_required
def view_profile(request):
    context_dict = {}

    username = request.user.username
    context_dict['username'] = username
    first_name = request.user.first_name
    context_dict['first_name'] = first_name
    last_name = request.user.last_name
    context_dict['last_name'] = last_name
    email = request.user.email
    context_dict['email'] = email

    return render(request, 'explorescotland/profile.html', context_dict)

def edit_profile(request):
    form = ProfileForm(instance=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save(commit=True)

            return HttpResponseRedirect(reverse('view_profile')) #Can redirect to confirmation page
        else:
            print(form.errors)

    return render(request, 'explorescotland/edit_profile.html', {'form': form})


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
