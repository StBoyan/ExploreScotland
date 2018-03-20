from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from explorescotland.forms import *
from explorescotland.models import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

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
            return HttpResponseRedirect(reverse('parent_area'))
        else:
            print(form.errors)

    return render(request, 'explorescotland/feedback.html', {'form': form})

@login_required
def view_profile(request):
    context_dict = {}
    # Gets user and ParentProfile instances
    user = request.user
    parent = ParentProfile.objects.get(user=user)

    context_dict['user'] = user
    context_dict['parent'] = parent

    return render(request, 'explorescotland/profile.html', context_dict)

@login_required
def edit_profile(request):
    context_dict ={}
    # Gets form for User attributes
    user_form = UserForm(instance=request.user)
    context_dict['user_form'] = user_form
    # Gets form for user's ParentProfile attributes
    parent = ParentProfile.objects.get(user=request.user)
    profile_form = ProfileForm(instance=parent)
    context_dict['profile_form'] = profile_form

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=parent)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save(commit=True)
            profile_form.save(commit=True)

            return HttpResponseRedirect(reverse('view_profile'))
        else:
            print(user_form.errors, profile_form.errors)

    return render(request, 'explorescotland/edit_profile.html', context_dict)

@login_required
def add_child(request):
    form = ChildForm()

    if request.method == 'POST':
        # Links current user to the child
        child = ChildProfile(parent=request.user)
        form = ChildForm(request.POST, instance=child)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('manage_children'))
        else:
            print(form.errors)

    return render(request, 'explorescotland/add_child.html', {'form': form})

@login_required
def manage_children(request):
    return render(request, 'explorescotland/manage_children.html', {})

@csrf_exempt
@login_required
def view_children(request):
    user = request.user
    children = user.childprofile_set.all()

    # Delete child profile upon button press
    if request.method == 'POST':
        child_name = request.POST.get('child', None)
        ChildProfile.objects.filter(name=child_name, parent=user).delete()

    return render(request, 'explorescotland/view_children.html', {'children': children})

def userHomePage (request):
    return render(request, 'explorescotland/userHomePage.html', {})

def scot (request):
    return render(request, 'explorescotland/personaScot.html', {})

def lily (request):
    return render(request, 'explorescotland/personaLily.html', {})

def googlemap(request):
    return render(request,'explorescotland/googlemap.html',{})

# Test AJAX thing to show you how it works
def test_ajax(request):
    return HttpResponse("This is text from the server!!")

def getQuestion(request):
    data = serializers.serialize('json', QuizQuestion.objects.all())
    return HttpResponse(data, content_type="application/json")

def get_level_information(request):
    level_id = None
    print("reeeequest", request)
    if request.method == 'GET':
        level_id = request.GET['level_id']

    text = ''
    if level_id:
        level = Level.objects.get(number=int(level_id))
        if level:
            text = level.content
            print("textttttt", text)


    return JsonResponse({'content' : text})
