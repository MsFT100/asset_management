from django.urls import path
from .views import branch_create, branch_list,  branch_edit , branch_details, branch_delete

urlpatterns = [
    # path('', branch_list, name="branch_list"),
    path('list/', branch_list, name="branch_list"),
    path('create/', branch_create, name="branch_create"),

    # TODO 
    path('<int:branch_id>/', branch_details, name="branch_details"),
    path('<int:branch_id>/edit/', branch_edit, name="branch_edit"),
     path('<int:branch_id>/delete/', branch_delete, name="branch_delete"),
]
