from django.shortcuts import render, redirect
from django.urls import reverse


from django.views.generic import ListView, DetailView

from .models import Sprint
from .sprint_forms import SprintForm

class SprintList(ListView):
    model = Sprint
    context_object_name = 'sprints'
    template_name = 'sprint/sprint_list.html'
    ordering = ['-start_date', ]
    
class SprintDetail(DetailView):
    model = Sprint    
    context_object_name = 'sprint'
    template_name = 'sprint/sprint_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(SprintDetail, self).get_context_data(**kwargs)
        sprint_tasks = Sprint.objects.get(pk=self.kwargs['pk']).sprint_tasks.all()
        tasks_completed = [task for task in sprint_tasks if 'complete' in task.status]
        if (len(sprint_tasks)):
            percentage_completed = len(tasks_completed)*100/len(sprint_tasks)
        else:
            percentage_completed = 0
        context['sprint_tasks'] = sprint_tasks
        context['total_no_of_tasks'] = len(sprint_tasks)
        context['tasks_completed'] = len(tasks_completed)
        context['percentage_completed'] = percentage_completed
        return context
    
def add_sprint(request):
    form = SprintForm()
    if request.method == "POST":
        form = SprintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('sprint_list'))
    context = {
        'form': form
    }
    return render(request, 'sprint/add_sprint.html', context=context)