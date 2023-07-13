from django.urls import path
from .views import device_create, device_details, device_edit, device_list, device_delete

urlpatterns = [
    # path('', device_list, name="device_list"),
    path('list/', device_list, name="device_list"),
    path('create/', device_create, name="device_create"),
    path('<int:device_id>/', device_details, name="device_details"),
    path('<int:device_id>/edit/', device_edit, name="device_edit"),
    path('<int:device_id>/delete/', device_delete, name="device_delete"),
]
