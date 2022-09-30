from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

class Task(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateTimeField(auto_now=True)
    effort_hours = models.PositiveIntegerField(default=2)
    status = models.CharField(max_length=50)
    date_completed = models.DateTimeField(auto_now=True)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now=True)
    time_spent = models.PositiveIntegerField(default=2)
    content_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey("content_type", "content_id")

    def __str__(self):
        return self.title


class Goal(models.Model):
    description = models.TextField(max_length=250)
    status = models.CharField(max_length=100)
    #objectives = models.ForeignKey(Objective, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Objective(models.Model):
    description = models.TextField(max_length=250)
    category = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=True, blank=True)
    completion_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=100)
    tasks = GenericRelation(Task)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.description

class Project(models.Model):
    type = models.CharField(max_length=100) # personal or office
    description = models.TextField(max_length=250)
    due_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100)
    effort_hours = models.PositiveIntegerField(default=10)
    completion_date = models.DateTimeField(auto_now=True)
    time_spent = models.PositiveIntegerField(default=0)
    tasks = GenericRelation(Task)


class Quotes(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20] + " ..."