from django.urls import path

from todo.views import (
    index,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    toggle_task_completion,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tag/", TagListView.as_view(), name="tags-list"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "task/toggle-completion/<int:pk>",
        toggle_task_completion,
        name="toggle-task-completion",
    ),
]

app_name = "todo"
