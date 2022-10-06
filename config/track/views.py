from django.shortcuts import render
from random import choice
from datetime import datetime
from django.utils import timezone

from track import models

def index(request):
    quote = choice(models.Quotes.objects.all())
    goals = models.Goal.objects.all()
    announcement = models.Announcements.objects.order_by('-date_added').first()
    this_quarter_objectives = models.Objective.objects.filter(due_date__gte = (timezone.now()), due_date__lte=(timezone.make_aware(datetime(2022, 11, 1))))
    weekly_tasks = models.Task.objects.exclude(status = 'complete')
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

def objective_detail(request, id):
    objective = models.Objective.objects.get(pk=id)
    goal = objective.goal
    return render(request, 'track/objective_detail.html', {'objective': objective, 'goal': goal})


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