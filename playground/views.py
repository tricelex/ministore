# from django.forms import DecimalField
from itertools import product

from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from django.db.models import DecimalField, ExpressionWrapper, F, Func, Q, Value
from django.db.models.aggregates import Count, Min
from django.db.models.functions import Concat
from django.shortcuts import render

from store.models import Customer, Order, OrderItem, Product
from tags.models import Tag, TaggedItem


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

    return render(request, "playground/hello.html", {"name": "Chiboy", "tags": list(query_set)})
