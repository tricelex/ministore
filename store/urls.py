from django.urls import path

from .views import collection_detail, collection_list, product_detail, product_list

urlpatterns = [
    path("products/", product_list, name="product_list"),
    path("products/<int:pk>/", product_detail, name="product_detail"),
    path("collections/", collection_list, name="collection_list"),
    path("collections/<int:pk>/", collection_detail, name="collection_detail"),
]
