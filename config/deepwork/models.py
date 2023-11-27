from django.db import models
from django.utils import timezone


class Deepwork(models.Model):
    date = models.DateField(default=timezone.now)
    work_hours = models.IntegerField(default=0)
    self_hours = models.IntegerField(default=0)
    studytopics_covered = models.TextField(blank=True, null=True)
    officework_done = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"deepwork on {self.date}"
    