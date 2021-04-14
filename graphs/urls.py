from django.urls import path
from . import views


urlpatterns = [
    path("connectNode/", views.connect_nodes),
    path("path/", views.path),
]
