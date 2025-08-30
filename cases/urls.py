# from django.urls import path
# from . import views


# app_name = "cases"

# urlpatterns = [
#     path("", views.case_list, name="case_list"),
#     path("<int:pk>/", views.case_detail, name="case_detail"),
#     path("new_form/", views.case_create_form, name="new_form"),
#     path("create/", views.case_create, name="create"),
# ]
# cases/urls.py
from django.urls import path
from . import views

app_name = "cases"

urlpatterns = [
    path("", views.case_list, name="case_list"),
    path("create/", views.case_create, name="case_create"),
    path("form/", views.case_form, name="case_form"),
]
