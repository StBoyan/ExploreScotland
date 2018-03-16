from django.conf.urls import url
from explorescotland import views

urlpatterns = [
    url(r'^test_ajax/', views.test_ajax, name='test_ajax'),
    url(r'^quizzes/', views.getQuestion, name='quizzes'),

    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^parent_area/', views.parent_area, name='parent_area'),   # TODO make all urls originating from parent area
    url(r'^feedback/', views.feedback, name='feedback'),            # have parent area as root url
    url(r'profile/edit/', views.edit_profile, name='edit_profile'),
    url(r'profile/', views.view_profile, name='view_profile'),
    url(r'children/view/', views.view_children, name='view_children'),
    url(r'children/add/', views.add_child, name='add_child'),
    url(r'children/', views.manage_children, name='manage_children'),
    url(r'^userHomePage/', views.userHomePage, name='homePage'),
    url(r'^personaScot/', views.scot, name='scot'),
    url(r'^personaLily/', views.lily, name='lily'),
    url(r'^googlemap/',views.googlemap,name='googlemap'),

]
