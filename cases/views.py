from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import DisputeCase
from .forms import DisputeCaseForm

# Create your views here.


# Case related views
def case_list(request):
    cases = (
        DisputeCase.objects.select_related("order").prefetch_related("returns").all()
    )
    if request.htmx:
        return render(request, "cases/case_table.html", {"cases": cases})
    return render(request, "cases/case_list.html", {"cases": cases})

def case_form(request):
    form = DisputeCaseForm()
    return render(request, "cases/case_form.html", {"form": form})

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




