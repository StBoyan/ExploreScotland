from django.conf.urls import url
from explorescotland import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/', views.parent_login, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^userHomePage/', views.userHomePage, name='homePage'),
    url(r'^personaScot/', views.scot, name='scot'),
    url(r'^personaLily/', views.lily, name='lily'),

]
