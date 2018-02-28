from django.conf.urls import url
from explorescotland import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
