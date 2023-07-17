# device/device_api/urls.py : API urls.py
from django.urls import path
from .views import (
    DeviceListApiView,
    DeviceDetailApiView
)

urlpatterns = [
    path('device', DeviceListApiView.as_view()),
    path('device/<int:device_id>/', DeviceDetailApiView.as_view()),
]
