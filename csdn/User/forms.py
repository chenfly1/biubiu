#coding:utf-8

import re
from django import forms
from django.forms import ValidationError,fields
from models import CMDBUser


class Register(forms.Form):
    username = forms.CharField(
        max_length=32,
        min_length=4,
        label="用户名",
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"用户名"}),
        error_messages={
            "required": "用户名不能为空",
            "min_length":"用户名最少4个字符",
        }
    )
    password = forms.CharField(
        max_length=32,
        min_length=6,
        label="密码",
        error_messages={
            "required": "密码不能为空",
            "min_length": "密码最少6个字符",
        },
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "密码"})
    )
    email = forms.CharField(
        max_length=32,
        min_length=4,
        label="邮箱",
        error_messages={
            "required": "邮箱不能为空",
            "min_length": "邮箱最少4个字符",
        },
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "邮箱"})
    )
    phone = forms.CharField(
        max_length=32,
        min_length=11,
        label="手机号",
        error_messages={
            "required": "手机号不能为空",
            "min_length": "手机号最少11个字符",
        },
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "手机号"})
    )
    photo = forms.ImageField(
        label="用户头像"

    )
    #
    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     if username.

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if password.isdigit():
            raise ValidationError("密码是由数字+字母+特殊字符组成的")
        elif password.isalnum():
            raise ValidationError("密码是由数字+字母+特殊字符组成的")
        else:
            return password

    def clean_email(self):
        email = self.cleaned_data.get("email")
        res = re.match(r"\w+@\w+\.[a-zA-Z]+", email)
        if res:
            return email
        else:
            raise ValidationError("邮箱格式错误")



