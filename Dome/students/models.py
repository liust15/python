from django.db import models
from django.contrib import admin  
# Create your models here.
class Toutiao(models.Model):
    id = models.CharField(u'编号', max_length=254,primary_key=True)
    image_url = models.URLField(u'图片地址',null=True)
    title = models.TextField(u'标题')
    media_creator_id = models.CharField(u'作者编号', max_length=254)
    media_name = models.TextField(u'作者昵称')

    def __unicode__(self):  
        return self.title  

class ToutiaoAdmin(admin.ModelAdmin):  
    list_display = ('id','image_url', 'title', 'media_creator_id', 'media_name')   


admin.site.register(Toutiao, ToutiaoAdmin)   