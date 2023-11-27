from django import forms

from track.models import Task, Objective

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        
class ObjectiveForm(forms.ModelForm):
    class Meta:
        model = Objective
        fields = '__all__'
        exclude = ('effort_hours', 'effort_left', 'progress')
        
        
class ObjectiveLookupForm(forms.Form):
    keyword = forms.CharField(max_length=100, required=False)
    objective_description = forms.CharField(max_length=150, required=False)