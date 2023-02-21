from django.urls import reverse_lazy
from django.views import generic

from tasks.models import Task, Tag


class IndexView(generic.ListView):
    model = Task
    queryset = Task.objects.all().prefetch_related("tag")
    template_name = "tasks/index.html"


class TagsListView(generic.ListView):
    model = Tag


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:index")
    template_name = "tasks/task_delete.html"


