from django.urls import path
from . import views

urlpatterns = [
    path("category/", views.Category1ListCreateView.as_view(), name="category_create"),
    path("category/<uuid:uuid>/", views.Category1RetrieveUpdateDeleteView.as_view(), name="category_modify"),
    path("news/", views.News1ListCreateView.as_view(), name="news_create"),
    path("reporter/", views.GetReporterNewsOnly.as_view(), name="reporter_news"),
    path("passing/<username>/", views.GetReporterNewsByparsingName.as_view(), name="reporter_news"),
    path("news/<uuid:uuid>/", views.News1RetrieveUpdateDeleteView.as_view(), name="new_modify"),
    # path("filter/", views.News1ListView.as_view(), name="filter"),
]