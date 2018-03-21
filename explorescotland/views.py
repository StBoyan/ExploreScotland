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
from explorescotland.decorators import child_is_selected

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
    # Gets current User and ParentProfile instances
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

    # If user wants to update profile information
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

@csrf_exempt
@login_required
def children_area(request):
    context_dict = {}
    user = request.user
    # Gets all children of current user
    children = user.childprofile_set.all()
    context_dict['children'] = children

    # Tries to get the name of the current child's session
    try:
        child_name = request.session['child_session']
    # If not assigned, assign None
    except KeyError:
        child_name = None

    # If there is a child's session, get the ChildProfile object
    # and its level
    if child_name is not None:
        child_instance = ChildProfile.objects.get(parent=user, name=child_name)
        context_dict['level'] = child_instance.level
    else:
        context_dict['level'] = None

    context_dict['child_session'] = child_name

    # If POST then update child session
    if request.method == 'POST':
        # get selected child name
        child_session = request.POST.get('child', None)
        # If child wants to log out, assign None
        if child_session == 'end':
            set_child_session(request, None)
        # Else assign the child name to the session
        else:
            set_child_session(request, child_session)
        return HttpResponseRedirect(reverse('children_area'))

    return render(request, 'explorescotland/children_area.html', context_dict)

@login_required
@child_is_selected
def scot (request):
    return render(request, 'explorescotland/personaScot.html', {})

@login_required
@child_is_selected
def lily (request):
    return render(request, 'explorescotland/personaLily.html', {})

@login_required
@child_is_selected
def googlemap(request):
    return render(request,'explorescotland/googlemap.html',{})

def getQuestion(request):
    data = serializers.serialize('json', QuizQuestion.objects.all())
    return HttpResponse(data, content_type="application/json")

def getChildLevel(request):
    child_name = request.session['child_session']
    child_instance = ChildProfile.objects.filter(parent=request.user, name=child_name)
    data = serializers.serialize('json', child_instance)
    return HttpResponse(data, content_type="application/json")

def get_level_information(request):
    level_id = None
    if request.method == 'GET':
        level_id = request.GET['level_id']

    text = ''
    if level_id:
        level = Level.objects.get(number=int(level_id))
        if level:
            text = level.content

    return JsonResponse({'content' : text})

def get_level_for_map(request):
    # Get child name from session
    child_name = request.session['child_session']
    # Get child object associated
    child = ChildProfile.objects.get(parent=request.user, name=child_name)
    level = child.level

    return JsonResponse({'currentLevel' : level})

# Set child session on the server
def set_child_session(request, child):
    if child is not None:
        request.session['child_session'] = child
    else:
        request.session['child_session'] = None

@csrf_exempt
# Store child's upgraded level
def store_level(request):
    child_name = request.session['child_session']
    child = ChildProfile.objects.get(parent=request.user,name=child_name)
    child.level = child.level + 1
    child.save()
    return JsonResponse({})
