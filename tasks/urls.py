from django.urls import path
from .views import Tasks, remove_from_todolist, update_task

app_name = "tasks"

urlpatterns = [
    path('', Tasks, name='tasks'),
    path('/<str:pk>', update_task, name="update_task"),
    path('/<str:pk>', remove_from_todolist, name="remove_from_todolist"),

]
