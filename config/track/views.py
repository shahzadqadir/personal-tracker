from django.shortcuts import render
from random import choice
from datetime import datetime
from django.utils import timezone

from track import models

def index(request):
    quote = choice(models.Quotes.objects.all())
    goals = models.Goal.objects.all()
    this_quarter_objectives = models.Objective.objects.filter(due_date__gte = (timezone.now()), due_date__lte=(timezone.make_aware(datetime(2022, 11, 1))))
    context = {
        'quote': quote,
        'author': quote.author,
        'goals': goals,
        'this_quarter_objectives': this_quarter_objectives
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
    
