"""ProTwo URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from AppTwo import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^help/', views.help, name='help'), # this will be mapped with any page with extension help/
    url(r'apptwo/', include('AppTwo.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^sa/', include('AppTwo.urls')), #on the place of sa we can any word what we want to use in browser.
    url(r'^basicapp/', include('basic_app.urls')),
    
]
