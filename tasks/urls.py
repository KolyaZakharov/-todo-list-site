from django.urls import path

from tasks.views import IndexView, TagsListView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "tags/",
        TagsListView.as_view(),
        name="tags"
    )

]



app_name = "tasks"