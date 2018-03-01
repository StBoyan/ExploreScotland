from django.conf.urls import url
from explorescotland import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^parent_area/', views.parent_area, name='parent_area'),
    url(r'^userHomePage/', views.userHomePage, name='homePage'),
    url(r'^personaScot/', views.scot, name='scot'),
    url(r'^personaLily/', views.lily, name='lily'),

]
