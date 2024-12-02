from django.db import models
from agarwood_server.utils import CommonAbstract, SeoAbstract 


class News(CommonAbstract, SeoAbstract):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')


    class Meta:
        verbose_name = 'Bài viết'
        verbose_name_plural = 'Bài viết'
        db_table = 'news'


    def __str__(self):
        return f"{self.id}"
    
