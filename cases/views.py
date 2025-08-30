from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import DisputeCase, Order, Return
from .forms import DisputeCaseForm, OrderForm, ReturnForm

# Create your views here.


# Case relatted views
def case_list(request):
    cases = (
        DisputeCase.objects.select_related("order").prefetch_related("returns").all()
    )
    if request.htmx:
        return render(request, "cases/case_table.html", {"cases": cases})
    return render(request, "cases/case_list.html", {"cases": cases})

@require_http_methods(["POST"])
def case_create(request):
    form = DisputeCaseForm(request.POST)
    if form.is_valid():
        case = form.save()
        cases = (
            DisputeCase.objects.select_related("order")
            .prefetch_related("returns")
            .all()
        )
        response = render(request, "cases/case_table.html", {"cases": cases})
        response["HX-Trigger"] = "caseCreated"
        return response
    else:
        return render(request, "cases/case_form.html", {"form": form}, status=400)


# Order rleated methods
def order_list(request):
    orders = Order.objects.all()
    if request.htmx:
        return render(request, "cases/order_table.html", {"orders": orders})
    return render(request, "cases/order_list.html", {"orders": orders})


@require_http_methods(["POST"])
def order_create(request):
    form = OrderForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect("order_list")


# Return related methods
def return_create(request):
    form = ReturnForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect("return_list")


def return_list(request):
    returns = Return.objects.select_related("order").all()
    form = ReturnForm()
    return render(request, "cases/return_list.html", {"returns": returns, "form": form})
