from django.db import models 
from agarwood_server.utils import CommonAbstract 
from .order import Order 
from .product import Product 


class OrderItem(CommonAbstract):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Đơn hàng')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name='Sản phẩm')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Số lượng')
    price = models.PositiveIntegerField(default=0, verbose_name='Đơn giá')


    class Meta:
        verbose_name = 'Chi tiết đơn hàng'
        verbose_name_plural = 'Chi tiết đơn hàng'
        db_table = 'order_items'

    
    def __str__(self):
        return f"{self.id} - {self.order}"
