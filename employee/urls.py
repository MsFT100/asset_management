from django.urls import path
from .views import employee_create, employee_list,  employee_edit , employee_details

urlpatterns = [
    # path('', employee_list, name="employee_list"),
    path('list/', employee_list, name="employee_list"),
    path('create/', employee_create, name="employee_create"),

    # TODO 
    path('<int:employee_id>/', employee_details, name="employee_details"),
    path('<int:employee_id>/edit/', employee_edit, name="employee_edit"),
    #path('<int:employee_id>/delete/', employee_delete, name="employee_delete"),
]
