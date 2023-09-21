from django.urls import path
from . import views


urlpatterns = [
    path("fetch/", views.fetch_external_news, name="fetch"),
    path("displayfetch/", views.fetch_news, name="fetch"),
]