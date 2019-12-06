#coding:utf-8
from django.db import models


# 用户
class CMDBUser(models.Model):
    username = models.CharField(max_length = 32,verbose_name = "用户名")
    password = models.CharField(max_length = 32, verbose_name = "密码")
    email = models.EmailField(verbose_name = "邮箱")
    phone = models.CharField(max_length = 32,verbose_name = "电话")
    photo = models.ImageField(upload_to = "images",verbose_name = "照片")
    #ImageField必须在安装pil或者pillow的基础上使用
    def __unicode__(self):
        return self.username




# 用户权限
class User_permission(models.Model):
    user_id = models.IntegerField(verbose_name="用户id")
    permission_id = models.IntegerField(verbose_name="权限id")


# 权限
class Permission(models.Model):
    name = models.CharField(max_length = 32,verbose_name = "权限名称")
    obj_id = models.IntegerField(verbose_name = "操作对象")
    description = models.TextField(verbose_name = "权限描述")

    def __unicode__(self):
        return self.name
# 组
class Group(models.Model):
    name = models.CharField(max_length = 32,verbose_name = "组名称")
    def __unicode__(self):
        return self.name


# 组权限
class Permission_group(models.Model):
    permission_id = models.IntegerField(verbose_name="权限id")
    group_id = models.IntegerField(verbose_name="组id")


# 用户和组
class User_group(models.Model):
    user_id = models.IntegerField(verbose_name="用户id")
    group_id = models.IntegerField(verbose_name="组id")
