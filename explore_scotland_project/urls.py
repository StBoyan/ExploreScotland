"""explore_scotland_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from django.contrib.auth import views
from explorescotland import views

# Redirect link upon successful registration
class MyRegistrationView(RegistrationView):
    def get_sucess_url(self, user):
        return '/explorescotland/'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^explorescotland/', include('explorescotland.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^auth/', include('social_django.urls', namespace='social')),

]
