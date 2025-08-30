from django.shortcuts import redirect, render
from .models import Order
from django.views.decorators.http import require_http_methods
from .forms import OrderForm

#to show all the orders
def order_list(request):
    orders = Order.objects.all()
    if request.htmx:
        return render(request, "orders/order_table.html", {"orders": orders})
    return render(request, "orders/order_list.html", {"orders": orders})


# to show the order form to create new order
def order_form(request):
    form = OrderForm()
    return render(request, "orders/order_form.html", {"form": form})

#show form to create new order  
@require_http_methods(["POST"])
def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            orders = Order.objects.all()
            response = render(request, "orders/order_list.html", {"orders": orders})
            response['HX-Trigger'] = 'orderCreated'
            return response
    else:
        return render(request, "orders/order_form.html", {"form": form}, status=400)
