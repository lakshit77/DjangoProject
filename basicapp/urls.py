from django.conf.urls import url

from . import views

app_name = "basicapp"

urlpatterns = [
    url("", views.SchoolListView.as_view(), name="list"),
    url("(?P<id>)/", views.SchoolDetailView.as_view(), name="detail"),
]
