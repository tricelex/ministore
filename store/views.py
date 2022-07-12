from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, QueryDict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer


# Create your views here.
@api_view(["GET"])
def product_list(request):
    queryset = Product.objects.select_related("collection").all()
    serializer = ProductSerializer(queryset, many=True, context={"request": request})
    return Response(serializer.data)


@api_view(["GET"])
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(["GET"])
def collection_detail(request, pk):
    # collection = get_object_or_404(Product, pk=id)
    # serializer = ProductSerializer(product)
    # return Response(serializer.data)
    return Response("data")
