from django.contrib import admin
from track import models


admin.site.register(models.Goal)
admin.site.register(models.Objective)
admin.site.register(models.Project)
admin.site.register(models.Task)
admin.site.register(models.Quotes)