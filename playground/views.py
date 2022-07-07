# from django.forms import DecimalField
from django.shortcuts import render
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Min
from store.models import Product, OrderItem, Order, Customer


def sayHello(request):
    discounted_price = ExpressionWrapper(
        F("unit_price") * 0.8, output_field=DecimalField()
    )

    query = Product.objects.annotate(
        discounted_price=discounted_price,
    )

    return render(
        request, "playground/hello.html", {"name": "Chiboy", "products": query}
    )
