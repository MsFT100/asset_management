from django import forms
from .models import Software
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


class SoftwareForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
           
           'license_key',
           'license_name',
           'license_email',
           'license_allocated',
           'license_type',
            'purchase_date',
            'purchase_order',
            'seats',
            'expiration_date',
            'purchase_cost',
            'supplier_id',
            'comments',
            Submit('submit', 'Save')
        )

    class Meta:
        model = Software
        fields = [
           'license_key',
           'license_name',
           'license_email',
           'license_allocated',
           'license_type',
           'purchase_date',
           'purchase_order',
           'seats',
           'expiration_date',
           'purchase_cost',
           'supplier_id',
           'comments',]
        widgets = {
            # 'comments': forms.TextInput(attrs={'cols': 80, 'rows': 20}),
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
            'purchase_order':  forms.DateInput(attrs={'type': 'date'}),
            'expiration_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            
        }
