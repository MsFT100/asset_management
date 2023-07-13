from django.urls import path
from .views import software_create, software_details, software_edit, software_list, software_delete

urlpatterns = [
    # path('', software_list, name="software_list"),
    path('list/', software_list, name="software_list"),
    path('create/', software_create, name="software_create"),
    path('<int:software_id>/', software_details, name="software_details"),
    path('<int:software_id>/edit/', software_edit, name="software_edit"),
    path('<int:software_id>/delete/', software_delete, name="software_delete"),
]
