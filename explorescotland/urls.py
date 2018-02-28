from django.conf.urls import url
from explorescotland import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^$', views.userHomePage, name='homePage'),
    url(r'^$', views.scot, name='Scot'),
    url(r'^$', views.lily, name='Lily'),

]
