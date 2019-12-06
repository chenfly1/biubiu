#coding:utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse
#from forms import Register
from models import *
from cmdb.views import getmd5,loginValid
from PIL import Image

@loginValid
def index(request):
    register = Register()

    return render(request,"account/index.html",locals())



#检查用户名是否重复
def valid_username(username):
    try:
        user = CMDBUser.objects.get(username=username)
    except:
        return username
    else:
        return "该用户已经被注册！"

def username_valid(request):
    result = {"type": "error", "data": ""}
    if request.method =="GET":
        username = request.GET["username"]
        res = valid_username(username)
        if username == res:
            result["type"] = "success"
            result["data"] = res
        else:
            result["type"] = "error"
            result["data"] = res
    else:
        result["data"] = "request must be get"
    return JsonResponse(result)

#检查邮箱是否重复
def valid_email(email):
    try:
        email = CMDBUser.objects.get(email=email)
    except:
        return email
    else:
        return "该邮箱已经被注册！"

def email_valid(request):
    result = {"type":"error","data":""}
    if request.method =="GET":
        email = request.GET["email"]
        res = valid_email(email)
        if email == res:
            result["type"] = "success"
            result["data"] = res
        else:
            result["type"] = "error"
            result["data"] = res
    else:
        result["data"] = "request must be get"
    return JsonResponse(result)

# 检查手机号是否重复
def valid_phone(phone):
    try:
        user = CMDBUser.objects.get(phone=phone)  # 尝试在数据库查询改手机号
    except:
        return phone  # 假如不存在，就返回手机号，可以注册
    else:
        return "该手机号已经被注册！"

def phone_valid(request):
    result = {"type": "error", "data": ""}
    if request.method == "GET":
        phone = request.GET["phone"]
        res = valid_phone(phone)
        if phone == res:
            result["type"] = "success"
            result["data"] = res
        else:
            result["type"] = "error"
            result["data"] = res
    else:
        result["data"] = "request must be get"
    return JsonResponse(result)



#用户注册
def register(request):
    result = {"type":"error","data":""}
    if request.method == "POST":
        reg = Register(request.POST,request.FILES)
        if reg.is_valid():
            cleand_data = reg.cleaned_data
            username = cleand_data["username"]
            password = cleand_data["password"]
            email = cleand_data["email"]
            phone = cleand_data["phone"]
            photo = cleand_data["photo"]

            user = CMDBUser()
            user.username = username
            user.password = getmd5(password)
            user.email =email
            user.phone = phone
            # 保存图片
            name = "static/images/"+photo.name
            img = Image.open(photo)
            img.save(name)

            user.photo = "images/"+photo.name
            user.save()
            result["type"] = "success"
        else:
            result["type"] = "error"
            result["data"] = reg.errors
    else:
        result["data"] = "request error"

    return JsonResponse(result)

# 用户登陆
def login(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = CMDBUser.objects.get(username=username)
        except:
            return redirect("/login")
        else:
            md5_password = getmd5(password)
            if user.password == md5_password:
                response = redirect("/index")  # 实例化响应
                response.set_cookie("username", user.username)  # 设置cookie
                request.session["username"] = user.username  # 设置session
                return response
            else:
                return redirect("/login")

    return render(request,"account/login.html",locals())

