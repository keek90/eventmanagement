from django import forms
from . models import Event1


class ApplicantForm(forms.ModelForm):
    class Meta:
        model=Event1
        fields=['full_name','email','phone']