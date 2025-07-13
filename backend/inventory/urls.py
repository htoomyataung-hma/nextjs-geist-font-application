from django.urls import include, path
from rest_framework import routers
from .views import WarehouseViewSet, PurchaseOrderViewSet, SaleOrderViewSet

router = routers.DefaultRouter()
router.register(r'warehouses', WarehouseViewSet)
router.register(r'purchase-orders', PurchaseOrderViewSet)
router.register(r'sale-orders', SaleOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
