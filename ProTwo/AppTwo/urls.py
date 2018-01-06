from django.conf.urls import url
from AppTwo import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^access_record/', views.access_record,  name='access_record'),
    url(r'^help/', views.help, name='help'),
    url(r'^users/', views.users, name='users'),
    url(r'^first_form/', views.form_name_view, name='first_form'),
]
