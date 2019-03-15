from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView, View

from . import models


# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"


class SchoolListView(ListView):
    context_object_name = "schools"
    # by default context name is school_list
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = "school_detail"
    # by default context name is school
    model = models.School
    template_name = "basicapp/school_detail.html"
