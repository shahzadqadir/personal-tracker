from django.db import models

status_choices = [
    '',
    'Not Started',
    'On Going',
    'Completed'    
]

class Sprint1(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.Choices(status_choices)
    comments = models.TextField(max_length=255)
    
    def __str__(self):
        return self.title