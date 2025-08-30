from django.urls import path
from . import views

app_name = "returns"

urlpatterns = [
    path("", views.return_list, name="return_list"),
    path("create/", views.return_create, name="return_create"),
    path("form/", views.return_form, name="return_form"),
]
