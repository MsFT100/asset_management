from django import forms
from .models import Department
from branch.models import Branch
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


class DepartmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'comment',
            'department_active',
            'branch',
            Submit('submit', 'Save')
        )

    class Meta:
        model = Department
        fields = ['name', 'comment', 'department_active', 'branch']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            #'comment': forms.TextInput(attrs={'class': 'form-control'}),
            'branch': forms.Select(attrs={'class': 'form-control'}),
            'department_active': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
