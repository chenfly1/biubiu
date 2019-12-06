#coding:utf-8
from django.db import models

class Desktops(models.Model):
    sn = models.CharField(max_length=80,verbose_name="设备编码",null=False)
    name = models.CharField(max_length=80,verbose_name="设备名称")
    brand = models.CharField(max_length=80,verbose_name="品牌")
    number = models.CharField(max_length=80,verbose_name="数量")
    type = models.CharField(max_length=80,verbose_name="型号")
    department = models.CharField(max_length=80,verbose_name="部门")
    user = models.CharField(max_length=80,verbose_name="使用人")
    statue = models.CharField(max_length=80,verbose_name="状态")
    location = models.CharField(max_length=80,verbose_name="所在位置")
    delivery_time = models.CharField(max_length=80,verbose_name="出厂时间")
    remark = models.CharField(max_length=80,verbose_name="备注")