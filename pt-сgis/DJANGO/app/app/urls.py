from django.contrib import admin
from django.urls import path, include

from hello import views
from bookstore import views as book
from bookstore import urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("about", views.about, kwargs = {
        "name":"Айрат",
        "age" : 30
        }),
    path("contact", views.contact),
    path("current_time", views.current_time),
    path("workdir", views.workdir),
    path("get_python_files", views.get_python_files),
    path("calc/<int:x1>/<int:x2>", views.calc),
    path("smart-calc/<str:data>", views.smart_calc),
    path("bookstore", include('bookstore.urls')),
    path("<path:unknown_data>", views.f404),
]

