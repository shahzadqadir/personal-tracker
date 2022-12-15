from django.contrib import admin
from django.urls import path, include

from .views import TimeTableView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('time_table/', TimeTableView.as_view(), name='time_table'),
    path('', include('track.urls')),
]
