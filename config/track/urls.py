from django.urls import path
from track import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gantt_chart/', views.load_gantt_chart, name='gantt_chart'),
    path('goals/', views.GoalsListView.as_view(), name='goals'),
    path('objectives/', views.objectives, name='objectives'),
    path('objectives/completed/', views.objectives_completed, name='objectives_completed'),
    path('objective/<int:id>/', views.objective_detail, name='objective_detail'),
    path('task/<int:id>/', views.task_detail, name='task_detail'),
    path('goal/<int:id>/', views.goal_detail, name='goal_detail'),
    path('tasks/due_today/', views.tasks_due_today, name='tasks_due_today'),
    path('tasks/add_task/', views.add_task, name='add_task'),
    path('objectives/<str:month>/', views.monthly_objectives, name='monthly_objectives'),
    path('projects/', views.list_projects, name='projects_list'),
]