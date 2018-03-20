from django.conf.urls import url
from explorescotland import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^parent_area/feedback/', views.feedback, name='feedback'),
    url(r'parent_area/profile/edit/', views.edit_profile, name='edit_profile'),
    url(r'parent_area/profile/', views.view_profile, name='view_profile'),
    url(r'parent_area/children/view/', views.view_children, name='view_children'),
    url(r'parent_area/children/add/', views.add_child, name='add_child'),
    url(r'parent_area/children/', views.manage_children, name='manage_children'),
    url(r'^parent_area/', views.parent_area, name='parent_area'),
    url(r'^userHomePage/', views.userHomePage, name='homePage'),
    url(r'^personaScot/', views.scot, name='scot'),
    url(r'^personaLily/', views.lily, name='lily'),
    url(r'^googlemap/',views.googlemap,name='googlemap'),
    url(r'^getLevelInformation/$',views.get_level_information, name ="get_level_information"),

    # Ajax Urls
    url(r'^test_ajax/', views.test_ajax, name='test_ajax'),
    url(r'^quizzes/', views.getQuestion, name='quizzes'),

]
