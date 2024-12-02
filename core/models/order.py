from django.db import models 
from agarwood_server.utils import CommonAbstract 
from django.contrib.auth.models import User 
import uuid 
from django.utils.timezone import now 


class Order(CommonAbstract):
    ORDER_STATUS_CHOICES = (
        (0, 'Pending'),
        (1, 'Processing'),
        (2, 'Shipped'),
        (3, 'Delivered'),
        (4, 'Cancelled')
    )

    PAYMENT_METHOD_CHOICES = (
        (0, 'Ship COD'),
        (1, 'Internet Banking')
    )

    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    transaction_id = models.UUIDField(default=uuid.uuid4, verbose_name='Mã giao dịch')
    order_code = models.CharField(max_length=20, unique=True, null=True, blank=True, verbose_name='Mã đơn hàng', editable=False) 
    status = models.SmallIntegerField(default=0, choices=ORDER_STATUS_CHOICES, verbose_name='Trạng thái đơn hàng') 
    total_price = models.IntegerField(default=0, verbose_name='Tổng tiền đơn hàng') 
    name = models.CharField(max_length=255, verbose_name='Họ tên khách hàng')
    address = models.TextField(verbose_name='Địa chỉ giao hàng')
    phone = models.CharField(max_length=15, verbose_name='Số điện thoại')
    email = models.EmailField(max_length=300, verbose_name='Email')
    payment_method = models.SmallIntegerField(default=0, choices=PAYMENT_METHOD_CHOICES, verbose_name='Phương thức thanh toán')


    class Meta:
        verbose_name = 'Đơn hàng'
        verbose_name_plural = 'Đơn hàng'
        db_table = 'orders'


    def __str__(self):
        return f"{self.id} - {self.order_code} - {self.status}"


    def save(self, *args, **kwargs):
        if not self.order_code:
            self.order_code = generate_order_code()
        super(Order, self).save(*args, **kwargs)


def generate_order_code():
    current_date = now()
    year = current_date.year 
    month = current_date.month
    prefix = f"ORD-{year}-{month:02d}"

    last_order_in_month = Order.objects.filter(order_code__startswith=prefix).order_by('-id').first()
    if last_order_in_month:
        last_sequence = int(last_order_in_month.order_code.split('-')[-1])
        new_sequence = last_sequence + 1
    else:
        new_sequence = 1
    
    return f"{prefix}-{new_sequence:07d}"