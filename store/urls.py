from django.urls import include, path
from rest_framework_nested import routers

from .views import CollectionViewSet, ProductViewSet, ReviewViewSet, CartViewSet

router = routers.DefaultRouter()
router.register("products", ProductViewSet, basename="products")
router.register("collections", CollectionViewSet, basename="collections")
router.register("carts", CartViewSet, basename="carts")

products_router = routers.NestedDefaultRouter(router, "products", lookup="product")
products_router.register("reviews", ReviewViewSet, basename="product-reviews")

# router.urls
urlpatterns = [
    path("", include(router.urls)),
    path("", include(products_router.urls))
    # path("products/", ProductList.as_view(), name="product_list"),
    # path("products/<int:pk>/", ProductDetail.as_view(), name="product_detail"),
    # path("collections/", CollectionList.as_view(), name="collection_list"),
    # path("collections/<int:pk>/", CollectionDetail.as_view(), name="collection_detail"),
]
