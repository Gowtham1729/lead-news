from django.urls import path

from . import views

urlpatterns = [
    path("api/news", views.get_news, name="get_news"),
    path("news/", views.LatestNewsView.as_view(), name="news"),
    path("", views.LatestNewsView.as_view(), name="news"),
    path("news/<slug:pk>", views.DetailView.as_view(), name="details"),
]
