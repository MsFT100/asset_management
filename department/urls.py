from django.urls import path
from .views import department_create, department_list,  department_edit , department_details, department_delete

urlpatterns = [

    path('list/', department_list, name="department_list"),
    path('create/', department_create, name="department_create"),
    path('<int:department_id>/', department_details, name="department_details"),
    path('<int:department_id>/edit/', department_edit, name="department_edit"),
    path('<int:department_id>/delete/', department_delete, name="department_delete"),
]
