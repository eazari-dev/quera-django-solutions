from .models import OrderItem
from django-shortcuts import get_object_or_404
from django.http import HttpResponse

def checkout(request, order_pk):
    order = get_object_or_404(OrderItem, pk=order_pk)
    total = order.quantity * order.product.price
    return HttpResponse({'total_price': '{:.2f}'.format(total)})
