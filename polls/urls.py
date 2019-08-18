from django.urls import path, include
from . import views

urlpatterns = [
    path(route='', view=views.index, name='index'),
]
