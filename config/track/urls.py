from django.urls import path
from track import views;

urlpatterns = [
    path('', views.index),
    path('objective/<int:id>/', views.objective_detail, name='objective_detail'),
]