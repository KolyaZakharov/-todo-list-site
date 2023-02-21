from django.urls import path

from tasks.views import IndexView, TagsListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "tags/",
        TagsListView.as_view(),
        name="tags"
    ),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
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


]



app_name = "tasks"