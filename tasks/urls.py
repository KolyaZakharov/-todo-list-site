from django.urls import path

from tasks.views import (
    IndexView,
    TagsListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagTaskListView,
    TagsCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tags/", TagsListView.as_view(), name="tags"),
    path("tags/create/", TagsCreateView.as_view(), name="tags-create"),
    path(
        "tags/<int:pk>/update",
        TagUpdateView.as_view(),
        name="tags-update",
    ),
    path(
        "tags/<int:pk>/delete",
        TagDeleteView.as_view(),
        name="tags-delete",
    ),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/<int:pk>/update",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "tasks/<int:pk>/delete",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),
    path(
        "tasks/<int:pk>/add/",
        TagTaskListView.as_view(),
        name="task-update-tag"
    ),
]

app_name = "tasks"
