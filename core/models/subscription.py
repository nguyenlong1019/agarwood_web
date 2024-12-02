from django.db import models
from agarwood_server.utils import CommonAbstract 


class Subscription(CommonAbstract):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    email = models.EmailField(max_length=255, verbose_name='Email', unique=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name='Địa chỉ IP')


    class Meta:
        verbose_name = 'Người đăng ký'
        verbose_name_plural = 'Người đăng ký'
        db_table = 'subscriptions'


    def __str__(self):
        return f"{self.id} - {self.email}"