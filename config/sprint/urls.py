from django.urls import path
from .views import SprintList, SprintDetail, add_sprint

urlpatterns = [
    path('', SprintList.as_view(), name='sprint_list'),
    path('add_sprint/', add_sprint, name='add_sprint'),
    path('<int:pk>/', SprintDetail.as_view(), name='sprint_detail'),
]
