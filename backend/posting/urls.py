from django.urls import path

from . import views

app_name = "posting"

urlpatterns = [
    path("", views.PostView.as_view()),
    path("update/", views.PostUpdateView.as_view()),
    path("delete/", views.PostDeleteView.as_view()),
]
