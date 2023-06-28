from django import forms
from .models import Branch
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


class BranchForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'location',
            'branch_active',
            Submit('submit', 'Save')
        )

    class Meta:
        model = Branch
        fields = ['name',  'location', 'branch_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'branch_active': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
