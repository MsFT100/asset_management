from django import forms
from .models import Company
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


class CompanyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'domain',
            'logo',
            'location',
            'email',
            'company_active',
            Submit('submit', 'Save')
        )

    class Meta:
        model = Company
        fields = ['name', 'domain', 'logo', 'location', 'email', 'company_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'domain': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'company_active': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
