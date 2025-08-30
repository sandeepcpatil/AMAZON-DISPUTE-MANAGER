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
    path("cases/", views.case_list, name="case_list"),
    path("cases/create/", views.case_create, name="case_create"),
    path("orders/", views.order_list, name="order_list"),
    path("orders/create/", views.order_create, name="order_create"),
    path("returns/", views.return_list, name="return_list"),
    path("returns/create/", views.return_create, name="return_create"),
]
