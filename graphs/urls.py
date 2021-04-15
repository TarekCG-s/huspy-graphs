from django.urls import path
from . import views


urlpatterns = [
    path("connect-node/", views.connect_nodes),
    path("path/", views.path),
]
