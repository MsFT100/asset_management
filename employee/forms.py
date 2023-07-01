from django import forms
from .models import employee
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


class employeeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'location',
            'gender',
            'address',
            'position',
            'department',
            Submit('submit', 'Save')
        )

    class Meta:
        model = employee
        fields = ['name',  'location', 'gender', 'address', 'position', 'department']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
        }
