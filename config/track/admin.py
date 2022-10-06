from django.contrib import admin
from track.models import Goal, Objective, Project, Task, Quotes, Announcements

class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ['description', 'goal', 'status', 'due_date']
    ordering = ('due_date', )

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'due_date']
    ordering = ('due_date',)

admin.site.register(Goal)
admin.site.register(Objective, ObjectiveAdmin)
admin.site.register(Project)
admin.site.register(Task, TaskAdmin)
admin.site.register(Quotes)
admin.site.register(Announcements)