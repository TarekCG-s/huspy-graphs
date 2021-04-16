from django.urls import path
from . import views


app_name = 'graphs'

urlpatterns = [
    path("connect-node/", views.connect_nodes, name="connect-node"),
    path("path/", views.path, name="path"),
]
