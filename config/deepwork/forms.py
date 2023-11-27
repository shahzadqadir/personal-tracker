from django import forms
from django.utils import timezone


"""
class Deepwork(models.Model):
    date = models.DateField(default=timezone.now)
    work_hours = models.IntegerField(default=0)
    self_hours = models.IntegerField(default=0)
    studytopics_covered = models.TextField(blank=True, null=True)
    officework_done = models.TextField(blank=True, null=True)
"""


class DeepworkForm(forms.Form):
    date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    work_time = forms.IntegerField()
    self_time = forms.IntegerField()
    studytopics_covered = forms.TextInput()
    officework_done = forms.TextInput()
