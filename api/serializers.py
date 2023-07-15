# todo/todo_api/serializers.py
from rest_framework import serializers
from device.models import Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ["id", "asset_tag", "model_id"]
