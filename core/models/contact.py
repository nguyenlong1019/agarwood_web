from django.db import models 
from agarwood_server.utils import CommonAbstract


class Contact(CommonAbstract):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255, verbose_name='Họ và tên')
    address = models.CharField(max_length=255, verbose_name='Địa chỉ')
    email = models.CharField(max_length=300, verbose_name='Email')
    phone = models.CharField(max_length=15, unique=True, verbose_name='Điện thoại')
    message = models.TextField(verbose_name='Nội dung liên hệ')


    class Meta:
        verbose_name = 'Liên hệ'
        verbose_name_plural = 'Liên hệ'
        db_table = 'contact'


    def __str__(self):
        return f"{self.id} - {self.phone}"
