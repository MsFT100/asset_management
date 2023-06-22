from django.urls import path
from .import views

urlpatterns = [
    path("", views.company_list, name='company_list'),
    path("create/", views.company_create, name='company_create'),
    path("edit/", views.company_edit, name='company_edit'),
]
