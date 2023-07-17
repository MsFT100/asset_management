# todo/todo_api/serializers.py
from rest_framework import serializers
from device.models import Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = [            
            'asset_tag',
            'model_id',
            'serial_no',
            'purchase_date',
            'asset_eol_date',
            'purchase_cost',
            'order_number',
            'assigned_to',
            'comments',
            'image',
            'physical',
            'status',
            'archived',
            'rtd_location_id',
            'warranty_months',
            'depreciate',
            'supplier_id',
            'last_checkout',
            'expected_checkin',
            'assigned_type',
            'last_audit_date',
            'next_audit_date',
            'byod',
            "company"
        ]
