from django.db import models

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    order_number = models.CharField(max_length=100, unique=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='purchase_orders')
    supplier = models.CharField(max_length=255)
    order_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.order_number

class SaleOrder(models.Model):
    order_number = models.CharField(max_length=100, unique=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='sale_orders')
    customer = models.CharField(max_length=255)
    order_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.order_number
