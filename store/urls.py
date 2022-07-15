from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CollectionViewSet, ProductViewSet

router = DefaultRouter()
router.register("products", ProductViewSet, basename="products")
router.register("collections", CollectionViewSet, basename="collections")
# router.urls

urlpatterns = [
    path("", include(router.urls))
    # path("products/", ProductList.as_view(), name="product_list"),
    # path("products/<int:pk>/", ProductDetail.as_view(), name="product_detail"),
    # path("collections/", CollectionList.as_view(), name="collection_list"),
    # path("collections/<int:pk>/", CollectionDetail.as_view(), name="collection_detail"),
]
