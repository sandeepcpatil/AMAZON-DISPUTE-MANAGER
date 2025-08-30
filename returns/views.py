from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from returns.models import Return
from .forms import ReturnForm

# Create your views here.


# Return related methods
def return_create(request):
    form = ReturnForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect("return_list")


def return_form(request):
    form = ReturnForm()
    return render(request, "returns/return_form.html", {"form": form})


@require_http_methods(["POST"])
def return_list(request):
    if request.method == "POST":
        form = ReturnForm(request.POST)
        if form.is_valid():
            form.save()
            forms = Return.objects.all()
            response = render(request, "returns/return_list.html", {"forms": forms})
            response["HX-Trigger"] = "returnCreated"
            return response
        else:
            return render(
                request, "returns/return_form.html", {"form": form}, status=400
            )
