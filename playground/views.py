# from django.forms import DecimalField
from itertools import product
from django.shortcuts import render
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Min
from store.models import Product, OrderItem, Order, Customer
from django.contrib.contenttypes.models import ContentType
from tags.models import Tag, TaggedItem
from django.db import transaction


def sayHello(request):

    order = Order()
    order.customer_id = 1
    order.save()

    item = OrderItem()
    item.order = order
    item.product_id = 1
    item.quantity = 1
    item.unit_price = 10
    item.save()

    return render(
        request, "playground/hello.html", {"name": "Chiboy", "tags": list(query_set)}
    )
