# from django.forms import DecimalField
from django.shortcuts import render
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Min
from store.models import Product, OrderItem, Order, Customer
from django.contrib.contenttypes.models import ContentType
from tags.models import Tag, TaggedItem


def sayHello(request):
    query_set = Product.objects.all()
    list(query_set)
    list(query_set)
    query_set[4]

    return render(
        request, "playground/hello.html", {"name": "Chiboy", "tags": list(query_set)}
    )
