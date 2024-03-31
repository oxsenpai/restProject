from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, CategoryViewSet, FirmViewSet, OrderViewSet, OrderItemViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('firms', FirmViewSet)
router.register('orders', OrderViewSet)
router.register('orderitems', OrderItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]