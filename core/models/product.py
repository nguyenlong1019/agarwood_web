from django.db import models 
from django.utils.text import slugify 
import random 
from agarwood_server.utils import CommonAbstract, SeoAbstract
from core.models.category import Category 
from core.models.product_type import ProductType 
from ckeditor_uploader.fields import RichTextUploadingField  
from django.dispatch import receiver 
import os 


class Product(CommonAbstract, SeoAbstract):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255, verbose_name='Tên sản phẩm')
    image = models.ImageField(upload_to='product_images/', null=True, blank=True, verbose_name='Ảnh sản phẩm', default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Danh mục')
    price = models.IntegerField(default=0, verbose_name='Giá')
    price_sale = models.IntegerField(null=True, blank=True, verbose_name='Giá sale')
    sku = models.CharField(max_length=15, unique=True, verbose_name='Mã sản phẩm')
    buy_counter = models.IntegerField(default=0, verbose_name='Số lượt mua')
    view_counter = models.IntegerField(default=0, verbose_name='Số lượt xem')
    description = RichTextUploadingField(null=True, blank=True, verbose_name='Mô tả')
    detail = RichTextUploadingField(null=True, blank=True, verbose_name='Chi tiết')
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, verbose_name='Loại sản phẩm')
    origin = models.CharField(max_length=255, verbose_name='Xuất xứ', default='Việt Name')
    guarantee = models.CharField(max_length=255, verbose_name='Thông tin bảo hành', default='2 năm')
    length = models.FloatField(default=0, verbose_name='Chiều dài (cm)')
    witdh = models.FloatField(default=0, verbose_name='Chiều rộng (cm)')
    weight = models.FloatField(default=0, verbose_name='Trọng lượng (gram)')
    height = models.FloatField(default=0, verbose_name='Chiều cao (cm)')
    size = models.CharField(max_length=255, null=True, blank=True, verbose_name='Kích thước shortcut')
    is_visible = models.BooleanField(default=True, verbose_name='Trạng thái hiển thị')
    is_sale = models.BooleanField(default=False, verbose_name='Sản phẩm sale')
    is_featured = models.BooleanField(default=False, verbose_name='Sản phẩm nổi bật')
    slug = models.SlugField(max_length=300, null=True, blank=True, unique=True, verbose_name='Slug')


    class Meta:
        verbose_name = 'Sản phẩm'
        verbose_name_plural = 'Sản phẩm'
        db_table = 'products'


    def __str__(self):
        return f"{self.id} - {self.name}"
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) + "_" + str(random.randrange(1000, 1000000))
        super(Product, self).save(*args, **kwargs)

    
    def get_absolute_url(self):
        return f"/products/{self.slug}.html"
    

@receiver(models.signals.post_delete, sender=Product)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=Product)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False 
    
    try:
        old_file = Product.objects.get(pk=instance.pk).image
    except Product.DoesNotExist:
        return False 
    
    new_file = instance.image 

    try:
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)
    except Exception as e:
        pass 

