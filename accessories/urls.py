from django.urls import path
from .views import accessories_create, accessories_details, accessories_edit, accessories_list, accessories_delete

urlpatterns = [
    # path('', accessories_list, name="accessories_list"),
    path('list/', accessories_list, name="accessories_list"),
    path('create/', accessories_create, name="accessories_create"),
    path('<int:accessories_id>/', accessories_details, name="accessories_details"),
    path('<int:accessories_id>/edit/', accessories_edit, name="accessories_edit"),
    path('<int:accessories_id>/delete/', accessories_delete, name="accessories_delete"),
]
