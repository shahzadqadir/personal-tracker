from django.urls import path
from track import views;

urlpatterns = [
    path('', views.index),
    path('objective/<int:id>/', views.objective_detail, name='objective_detail'),
    path('goal/<int:id>/', views.goal_detail, name='goal_detail'),
]