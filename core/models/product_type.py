from django.db import models 
from agarwood_server.utils import CommonAbstract


class ProductType(CommonAbstract):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255, verbose_name='Tên loại sản phẩm')


    class Meta:
        verbose_name = 'Loại sản phẩm'
        verbose_name_plural = 'Loại sản phẩm'
        db_table = 'product_type'


    def __str__(self):
        return f"{self.id} - {self.name}"
    
