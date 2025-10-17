from django import forms
from emp.models import employee

class employeeform(forms.ModelForm):
    class Meta:
        model=employee
        fields='__all__'