from django.urls import path

from . import views

urlpatterns = [
  path('hellowold/', views.helloWorld),
  path('', views.taskList, name='task-list'),
  path('task/<int:id>', views.tasKView, name="task-view"),
  path('newtask/', views.newTask, name="new-task"),
  path('yourname/<str:name>', views.yourName, name='your-name'),
]
