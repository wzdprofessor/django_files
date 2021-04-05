from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=32,verbose_name='文件名')
    #files = models.FileField(verbose_name='文件',max_length=128)
    files = models.ImageField(verbose_name='文件', max_length=128)


class OSS(models.Model):
    name = models.CharField(max_length=32,verbose_name='文件名')
    files = models.FileField(max_length=123,verbose_name='文件')



