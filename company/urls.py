from django.urls import path
from .views import company_create, company_details, company_edit, company_list ,company_delete

urlpatterns = [
    # path('', company_list, name="company_list"),
    path('list/', company_list, name="company_list"),
    path('create/', company_create, name="company_create"),
    path('<int:company_id>/', company_details, name="company_details"),
    path('<int:company_id>/edit/', company_edit, name="company_edit"),
    path('<int:company_id>/delete/', company_delete, name="company_delete"),
]
