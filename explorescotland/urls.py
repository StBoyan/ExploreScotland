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
    url(r'^children_area/', views.children_area, name='children_area'),
    url(r'^personaScot/', views.scot, name='scot'),
    url(r'^personaLily/', views.lily, name='lily'),
    url(r'^googlemap/',views.googlemap,name='googlemap'),

    # Ajax Urls
    url(r'^quizzes/', views.getQuestion, name='quizzes'),
    url(r'^level/', views.getChildLevel, name='level'),
    url(r'^getLevelInformation/$', views.get_level_information, name="get_level_information"),
    url(r'^getLevelForMap/$', views.get_level_for_map, name="get_level_for_map"),
    url(r'^levelUp/$', views.store_level, name="levelUp"),



]
