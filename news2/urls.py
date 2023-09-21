from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("details/<int:pk>/", views.details, name="single"),
    path("category/", views.category, name="category"),
    path("contact/", views.contact, name="contact"),
]