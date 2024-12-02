from django.db import models 
from agarwood_server.utils import CommonAbstract 
from core.models.product import Product 
import os 
from django.dispatch import receiver 


class ProductImage(CommonAbstract):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    image = models.ImageField(upload_to='product_images/', null=True, blank=True, verbose_name='Ảnh')
    desc = models.CharField(max_length=255, verbose_name='Văn bản thay thế', default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Sản phẩm')


    class Meta:
        verbose_name = 'Hình ảnh sản phẩm'
        verbose_name_plural = 'Hình ảnh sản phẩm'
        db_table = 'product_images'


    def __str__(self):
        return f"{self.id} - {self.name}"


@receiver(models.signals.post_delete, sender=ProductImage)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=ProductImage)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False 
    
    try:
        old_file = ProductImage.objects.get(pk=instance.pk).image
    except ProductImage.DoesNotExist:
        return False 
    
    new_file = instance.image 

    try:
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)
    except Exception as e:
        pass 