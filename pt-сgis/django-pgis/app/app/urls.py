"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from bookstore import views
from bookstore.views import  (
    current_time, workdir, filelist, calculator,
    f404,smart_calc, get_requests, json_response)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('current_time', current_time, name='current_time'),
    path('workdir', workdir, name='workdir'),
    path('filelist', filelist, name='filelist'),   
    path('calculator/<int:val_1>/<int:val_2>', calculator, name='calculator'),
    path('smart_calc/<str:string>', smart_calc, name='smart_calc'),
    path('requests', get_requests, name='requests'),
    path('json_response', json_response, name='json_response'),
    path('bookstore/', include('bookstore.urls')),
    path('<path:info>', f404, name='f404'),


]
