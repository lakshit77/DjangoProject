from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
    View,
)

from . import models


# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"


class SchoolListView(ListView):
    context_object_name = "schools"
    # by default context name is school_list
    model = models.School


class SchoolDetailView(DetailView):
    model = models.School
    context_object_name = "school_detail"
    # by default context name is school
    template_name = "basicapp/school_detail.html"


class SchoolCreateView(CreateView):
    model = models.School
    fields = ("name", "principal", "location")


class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ("name", "principal")


class SchoolDeleteView(DeleteView):
    context_object_name = "school_delete"
    model = models.School
    success_url = reverse_lazy("basicapp:list")
