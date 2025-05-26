from django.urls import path
# import bookstore.views
from . import views



urlpatterns = [
    path("", views.add_book),
    path("/about", views.about),   
    ]