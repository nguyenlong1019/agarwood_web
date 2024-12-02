from django.db import models 
from django.utils import timezone 


class CommonAbstract(models.Model):
    created_at = models.DateTimeField(editable=False, null=True, blank=True, verbose_name='Thời điểm tạo')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Thời điểm cập nhật')


    class Meta:
        abstract = True 
        ordering = ('-created_at',)


    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        super(CommonAbstract, self).save(*args, **kwargs)


class SeoAbstract(models.Model):
    meta_title = models.TextField(blank=True, null=True, verbose_name='SEO Title')
    meta_description = models.TextField(blank=True, null=True, verbose_name='SEO Description')
    meta_keywords = models.CharField(max_length=255, blank=True, null=True, verbose_name='SEO Keywords ')


    class Meta:
        abstract = True 


