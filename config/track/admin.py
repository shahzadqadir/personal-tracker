from django.contrib import admin
from track.models import Goal, Objective, Project, Task, Quotes

class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ['description', 'goal', 'status', 'due_date']
    ordering = ('due_date', )


admin.site.register(Goal)
admin.site.register(Objective, ObjectiveAdmin)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Quotes)