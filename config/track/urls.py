from django.urls import path
from track import views

urlpatterns = [
    path('', views.index, name='index'),
    path('progress/', views.progress, name='progress'),
    path('gantt_chart/', views.load_gantt_chart, name='gantt_chart'),
    path('objectives/', views.objectives, name='objectives'),
    path('objectives/search', views.objective_search, name='objectives_search'),
    path('goals/', views.goals, name='goals'),
    path('objectives/completed/', views.objectives_completed, name='objectives_completed'),
    path('objective/<int:id>/', views.objective_detail, name='objective_detail'),
    path('objective/<int:id>/edit', views.edit_objective, name='objective_edit'),
    path('task/<int:id>/', views.task_detail, name='task_detail'),
    path('task/<int:id>/edit', views.edit_task, name='edit_task'),
    path('task/<int:id>/delete', views.TaskDeleteView.as_view(), name='task_delete'),
    path('goal/<int:id>/', views.goal_detail, name='goal_detail'),
    path('tasks/', views.TaskListView.as_view(), name='tasks'), # don't include completed/cancelled
    path('tasks/all', views.AllTaskListView.as_view(), name='all_tasks'),
    path('tasks/due_today/', views.tasks_due_today, name='tasks_due_today'),
    path('tasks/add_task/', views.add_task, name='add_task'),
    path('objectives/<str:month>/', views.monthly_objectives, name='monthly_objectives'),
    path('projects/', views.list_projects, name='projects_list'),
]