from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.conf.urls import url

app_name = "app_turtle"

urlpatterns = [
    path("turtle/", views.view_turtle, name="turtle"),
]