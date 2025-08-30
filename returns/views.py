from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from returns.models import Return
from .forms import ReturnForm

# Create your views here.


# Return related methods
def return_list(request):
    returns = Return.objects.all()
    if request.htmx:
        return render(request, "returns/return_table.html", {"returns": returns})
    return render(request, "returns/return_list.html", {"returns": returns})


def return_form(request):
    form = ReturnForm()
    return render(request, "returns/return_form.html", {"form": form})


@require_http_methods(["POST"])
def return_create(request):
    if request.method == "POST":
        form = ReturnForm(request.POST)
        if form.is_valid():
            form.save()
            returns = Return.objects.all()
            response = render(request, "returns/return_list.html", {"returns": returns})
            response["HX-Trigger"] = "returnCreated"
            return response
        else:
            return render(
                request, "returns/return_form.html", {"form": form}, status=400
            )
