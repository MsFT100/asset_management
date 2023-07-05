from django import forms
from .models import Device
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


class DeviceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            
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
            'user_id',
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
            
            Submit('submit', 'Save')
        )

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
            'byod']
        widgets = {
            # 'comments': forms.TextInput(attrs={'cols': 80, 'rows': 20}),
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
            'asset_eol_date': forms.DateInput(attrs={'type': 'date'}),
            'image': forms.FileInput(),
            'last_checkout': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'expected_checkin': forms.DateInput(attrs={'type': 'date'}),
            'last_audit_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'next_audit_date': forms.DateInput(attrs={'type': 'date'}),
        }
