from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
    url(r'^base/$',views.base, name='base'),
    url(r'^register/$',views.register, name='register'),
    url(r'^user_login/$',views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^special/',views.special,name='special'),
]
