from django.urls import path

from .views import (
    collection_detail,
    collection_list,
    ProductList,
    ProductDetail,
)

urlpatterns = [
    path("products/", ProductList.as_view(), name="product_list"),
    path("products/<int:pk>/", ProductDetail.as_view(), name="product_detail"),
    path("collections/", collection_list, name="collection_list"),
    path("collections/<int:pk>/", collection_detail, name="collection_detail"),
]
