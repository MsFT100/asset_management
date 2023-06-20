from django import forms
from .models import Company
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

class CompanyForm(forms.ModelForm):
    def __init__(self, * args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit','Submit'))

        self.helper.layout = Layout(
            Field('name', css_class='form-control'),
        )
    class Meta:
        model = Company
        # fields = "__all__"

        fields =[
            "name"
        ]