import plotly.express as plt
import datetime
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from deepwork.forms import DeepworkForm
from .models import Deepwork

def main(request):
    
    workdone_list = []
    for i in range(1, 8):
        try:
            workdone = Deepwork.objects.get(date=datetime.date.today() - datetime.timedelta(days=i)).work_hours
            career = Deepwork.objects.get(date=datetime.date.today() - datetime.timedelta(days=i)).self_hours
            day = Deepwork.objects.get(date=datetime.date.today() - datetime.timedelta(days=i)).date.strftime("%A")
            workdone_list.append((day, workdone, career))
        except:
            workdone_list.append((0, 0, 0))
    print(workdone_list)   

        
    if request.method == 'POST':
        form = DeepworkForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            work_hours = form.cleaned_data['work_time']
            self_hours = form.cleaned_data['self_time']
            Deepwork.objects.create(date=date, work_hours=work_hours, self_hours=self_hours)
            messages.success(request, 'Deepwork hours saved successfully.')
            return HttpResponseRedirect(reverse('deepwork_main'))
    else:
        form = DeepworkForm()
            
    return render(request, 'deepwork/main.html', {'form': form})
