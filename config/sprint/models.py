from django.db import models

class Sprint(models.Model):
    choices = [
        ('not-started', 'Not Started'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'cancelled'),
    ]
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, default='not-started', choices=choices)
    comments = models.TextField(null=True, blank=True, max_length=1000)
    
    def __str__(self):
        return self.title
