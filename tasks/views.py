from django.views import generic

from tasks.models import Task, Tag


class IndexView(generic.ListView):
    model = Task
    queryset = Task.objects.all().prefetch_related("tag")
    template_name = "tasks/index.html"


class TagsListView(generic.ListView):
    model = Tag
