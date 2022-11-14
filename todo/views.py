from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm
from todo.models import Task, Tag


def index(request):
    tasks = Task.objects.all()

    context = {
        "tasks": tasks,
    }

    return render(request, "todo/index.html", context)


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tags-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tags-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tags-list")


class TaskCreateView(generic.CreateView):
    form_class = TaskForm
    model = Task
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(generic.UpdateView):
    form_class = TaskForm
    model = Task
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")


def toggle_task_completion(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = not task.completed
    task.save()

    return HttpResponseRedirect(reverse_lazy("todo:index"))
