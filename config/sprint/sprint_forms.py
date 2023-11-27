from django import forms
from .models import Sprint


class SprintForm(forms.ModelForm):
    class Meta:
        model = Sprint
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-control', 'type': 'date'}),
        }
