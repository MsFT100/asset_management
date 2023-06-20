from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name='company_index'),
    path("create/", views.create, name='company_create'),
]
