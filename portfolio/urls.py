from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("download_resume", views.download_resume, name="download_resume"),
]