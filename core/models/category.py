from django.db import models
from django.utils.text import slugify 
from agarwood_server.utils import CommonAbstract 


class Category(CommonAbstract):
    id = models.SmallAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255, verbose_name='Tên danh mục')
    desc = models.TextField(null=True, blank=True, verbose_name='Mô tả')
    slug = models.SlugField(max_length=300, null=True, blank=True, unique=True, verbose_name='Slug') 


    class Meta:
        verbose_name = 'Danh mục'
        verbose_name_plural = 'Danh mục'
        db_table = 'categories'


    def __str__(self):
        return f"{self.id} - {self.name}"
    

    def get_absolute_url(self):
        return f"/collections/{self.slug}"
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

