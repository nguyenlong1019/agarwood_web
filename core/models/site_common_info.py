from django.db import models 
from agarwood_server.utils import CommonAbstract 
import os 
from django.dispatch import receiver 


class SiteCommonInfo(CommonAbstract):
    id = models.SmallAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    logo = models.ImageField(upload_to='site_logo/', null=True, blank=True, verbose_name='Logo', default='')
    hotline = models.CharField(max_length=15, null=True, blank=True, verbose_name='Hotline')
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Số điện thoại')
    facebook_link = models.URLField(null=True, blank=True, verbose_name='Facebook Link')
    youtube_link = models.URLField(null=True, blank=True, verbose_name='Youtube Link')
    twitter_link = models.URLField(null=True, blank=True, verbose_name='Twitter Link')
    zalo_link = models.URLField(null=True, blank=True, verbose_name='Zalo Link')
    address = models.TextField(null=True, blank=True, verbose_name='Địa chỉ')
    email = models.EmailField(null=True, blank=True, verbose_name='Email')
    business_reg_info = models.TextField(null=True, blank=True, verbose_name='Thông tin đăng ký kinh doanh')


    class Meta:
        verbose_name = 'Thông tin chung'
        verbose_name_plural = 'Thông tin chung'
        db_table = 'site_common_info'


    def __str__(self):
        return f"{self.id}"


@receiver(models.signals.post_delete, sender=SiteCommonInfo)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.logo:
        if os.path.isfile(instance.logo.path):
            os.remove(instance.logo.path) 

    
@receiver(models.signals.pre_save, sender=SiteCommonInfo)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False 
    
    try:
        old_file = SiteCommonInfo.objects.get(pk=instance.pk).logo 
    except SiteCommonInfo.DoesNotExist:
        return False 
    
    new_file = instance.logo 

    try:
        if not old_file == new_file:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)
    except Exception as e:
        pass 

