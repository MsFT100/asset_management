from django import forms
from .models import Accessories
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


class AccessoriesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'description',
            'price',
            'image',
            'company',
            Submit('submit', 'Save')
        )

    class Meta:
        model = Accessories
        fields = ['name',  'description', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(),
            'company': forms.Select(attrs={'class': 'form-control'}),
        }
