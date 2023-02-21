from django.urls import path

from tasks.views import IndexView, TagsListView, TaskCreateView

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
    )

]



app_name = "tasks"