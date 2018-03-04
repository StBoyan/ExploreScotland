from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from explorescotland.forms import FeedbackForm
from explorescotland.models import Feedback
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
        form = FeedbackForm(request.POST, instance=feedback) #Can make this redirect to a thank you page

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('parent_area'))
        else:
            print(form.errors)

    return render(request, 'explorescotland/feedback.html', {'form': form})

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
