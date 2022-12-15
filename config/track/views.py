from django.shortcuts import render
from random import choice
from datetime import datetime
from django.utils import timezone

from django.views.generic import ListView

from track.forms import TaskForm

from track import models

def index(request):
    quote = choice(models.Quotes.objects.all())
    goals = models.Goal.objects.all()
    announcement = models.Announcements.objects.order_by('-date_added').first()
    this_quarter_objectives = models.Objective.objects.filter(due_date__gte = (timezone.make_aware(datetime(2022, 8, 1))), 
                                                              due_date__lte=(timezone.make_aware(datetime(2023, 2, 1)))).order_by('status')
    this_quarter_objectives = this_quarter_objectives.exclude(status__contains='complete')
    weekly_tasks = models.Task.objects.filter(due_date__gte = (timezone.make_aware(datetime(2022, 11, 14))),
                                              due_date__lte = (timezone.make_aware(datetime(2022, 11, 20))))
    weekly_tasks = weekly_tasks.exclude(status = 'complete').exclude(status__contains='cancelled').order_by('due_date')
    tasks_completed_this_week = ''
    context = {
        'quote': quote,
        'author': quote.author,
        'goals': goals,
        'announcement': announcement,
        'this_quarter_objectives': this_quarter_objectives,
        'weekly_tasks': weekly_tasks,
    }
    return render(request, 'track/index.html', context)


def objectives(request):
    objectives = models.Objective.objects.all()
    return render(request, 'track/objectives.html', {'objectives': objectives})


def objectives_completed(request):
    objectives = models.Objective.objects.filter(status__contains='complete')
    return render(request, 'track/objectives_completed.html', {'objectives': objectives})

def objective_detail(request, id):
    objective = models.Objective.objects.get(pk=id)
    goal = objective.goal
    tasks = objective.tasks.all()
    even_tasks = [task for num,task in enumerate(tasks) if num%2==0]
    odd_tasks = [task for num,task in enumerate(tasks) if num%2==1]
    total_time_spent = sum([task.time_spent for task in tasks if task.time_spent is not None])
    context = {
        'objective': objective,
        'goal': goal,
        'tasks': tasks,
        'even_tasks': even_tasks,
        'odd_tasks': odd_tasks,
        'total_time_spent': total_time_spent
    }
    return render(request, 'track/objective_detail.html', context=context)


def goal_detail(request, id):
    goal = models.Goal.objects.get(pk=id)
    objectives = goal.objective_set.all()
    return render(request, 'track/goal_detail.html', {'goal': goal, 'objectives': objectives})


def task_detail(request, id):
    task = models.Task.objects.get(pk=id)
    return render(request ,'track/task_detail.html', {'task': task})


def tasks_due_today(request):
    tasks = models.Task.objects.filter(due_date__date = timezone.now().date())
    return render(request, 'track/tasks_due_today.html', {'tasks': tasks})
    
def list_projects(request):
    projects = models.Project.objects.all()
    return render(request, 'track/projects_list.html', {'projects': projects})


def monthly_objectives(request, month):
    messages = []
    if 'nov' in month.lower():
        monthly_objectives = models.Objective.objects.filter(due_date__gte = (timezone.make_aware(datetime(2022, 11, 1))),
                                                             due_date__lte = (timezone.make_aware(datetime(2022, 12, 4)))).order_by('status')
        messages.append('Advanced Django - build a blog started this month is ending in December.')      
    elif 'dec' in month.lower():
        monthly_objectives = models.Objective.objects.filter(due_date__gte = (timezone.make_aware(datetime(2022, 12, 5))),
                                                             due_date__lte = (timezone.make_aware(datetime(2023, 1, 1)))).order_by('status')
        messages.append('Java: Data Structures course started this month will be ending in January')
    elif 'jan' in month.lower():
        monthly_objectives = models.Objective.objects.filter(due_date__gte = (timezone.make_aware(datetime(2023, 1, 2))),
                                                             due_date__lte = (timezone.make_aware(datetime(2023, 2, 5)))).order_by('status')
    elif 'feb' in month.lower():
        monthly_objectives = models.Objective.objects.filter(due_date__gte = (timezone.make_aware(datetime(2023, 2, 6))),
                                                             due_date__lte = (timezone.make_aware(datetime(2023, 3, 1)))).order_by('status')        
    elif 'mar' in month.lower():
        monthly_objectives = models.Objective.objects.filter(due_date__gte = (timezone.make_aware(datetime(2023, 3, 1))),
                                                             due_date__lte = (timezone.make_aware(datetime(2023, 4, 1)))).order_by('status')
    elif 'apr' in month.lower():
        monthly_objectives = models.Objective.objects.filter(due_date__gte = (timezone.make_aware(datetime(2023, 4, 2))),
                                                             due_date__lte = (timezone.make_aware(datetime(2023, 5, 1)))).order_by('status')
    elif 'may' in month.lower():
        monthly_objectives = models.Objective.objects.filter(due_date__gte = (timezone.make_aware(datetime(2023, 5, 2))),
                                                             due_date__lte = (timezone.make_aware(datetime(2023, 6, 1)))).order_by('status')
    else:
        monthly_objectives = ("This month is not defined yet.",)
        
    context = {
        'month': month.title(),
        'monthly_objectives': monthly_objectives,
        'messages': messages
    }
    return render(request, 'track/monthly_objectives.html', context=context)

class GoalsListView(ListView):
    model = models.Goal
    context_object_name = 'goals'
    template_name = 'track/goals.html'
    
def add_task(request):    
    form = TaskForm()    
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            print('test')
    return render(request, 'track/add_task.html', {'form': form})

def load_gantt_chart(request):
    return render(request, 'track/gantt.html')
        
    