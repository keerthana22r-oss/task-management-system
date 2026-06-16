from django.urls import path 
from . import views 
urlpatterns=[ 
path('home/',views.home, name='home'),
path('',views.read_task, name='read_task'),
path('update_task/<int:pk>/',views.update_task, name='update_task'),
path('delete_task/<int:pk>/',views.delete_task, name='delete_task'),
# base/urls.py
path('check-alerts/', views.check_task_alerts, name='check_alerts'),


]