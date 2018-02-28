from django.shortcuts import render
from explorescotland.forms import ParentForm, ParentProfileForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

def home(request):
    return render(request, 'explorescotland/home.html', {})

def signup(request):
    registered = False

    if request.method == 'POST':
        user_form = ParentForm(data=request.POST)
        profile_form = ParentProfile(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = ParentForm()
        profile_form = ParentProfileForm()

    return render(request,
                'explorescotland/signup.html',
                {'user_form': user_form,
                'profile_form': profile_form,
                'registered': registered})

def parent_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home')) # Need to change this to whatever page users are taken after logging in
            else:
                return HttpResponse("Your Explore Scotland account is disabled.")
        else:
            return HttpResponse("Invalid username or password. Please try again.")
    else:
        return render(request, 'explorescotland/login.html', {})
# Further functions need to be decorated with login_required eventually
def parentlogin(request):
    return render(request,'explorescotland/parentlogin.html',{})
def userHomePage (request):
    return render(request, 'explorescotland/userHomePage.html', {})

def scot (request):
    return render(request, 'explorescotland/personaScot.html', {})

def lily (request):
    return render(request, 'explorescotland/personaLily.html', {})
