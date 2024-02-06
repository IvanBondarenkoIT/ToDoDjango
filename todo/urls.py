from django.urls import path, include
from . import views

urlpatterns = [
    # Add task
    path("addTask/", views.add_task, name="addTask"),
    # Mark as done
    path("mark_as_done/<int:pk>", views.mark_as_done, name="mark_as_done"),
    # Mark as undone
    path("mark_as_undone/<int:pk>", views.mark_as_undone, name="mark_as_undone"),
    # EDIT Feature
    path("edit_task/<int:pk>", views.edit_task, name="edit_task"),
]
