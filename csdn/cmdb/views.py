#coding:utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse
import hashlib
from User.models import CMDBUser

# 密码加密
def getmd5(password):
    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()

def base(request):
    return render(request,"base.html",locals())

# COOKIES sessions验证
def loginValid(fun):
    def inner(request,*args,**kwargs):
        cookie = request.COOKIES
        c_username = cookie.get("username")
        s_username = request.session.get("username")
        if c_username and s_username and c_username == s_username:
            return fun(request,*args,**kwargs)
        else:
            return redirect("/login")
    return inner

# 登出--删除 cookies session
def logout(request):
    c_username = request.COOKIES.get("username")
    s_username = request.session.get("username")
    if c_username and s_username:
        del request.COOKIES["username"]
        del request.session["username"]
    return redirect("/login")


# 用户个人中心-现实个人信息
def user_settings(request):
    result = {"type":"error","data":""}
    if request.method == "GET":
        try:
            username = request.session.get("username")
            user = CMDBUser.objects.get(username=username)
        except:
            result["data"] = "Please login and then access the link."
            return JsonResponse(result)
        else:

            result["type"] = "success"
            result["data"] = {
                "username":user.username,
                "password":user.password,
                "email":user.email,
                "phone":user.phone,
                "photo":user.photo.name
            }
    else:
        result["data"] = "request error"
    return JsonResponse(result)

#用户修改密码等个人信息
def update_userinfo(request):
    result = {"type": "error", "data": ""}
    if request.method == "POST":
        u = request.session.get("username")
        if u:
            CMDBUser.objects.filter(username=u).update(
                username=request.POST["username"],
                password=request.POST["password"],
                email=request.POST["email"],
                phone=request.POST["phone"],
            )
            result["type"] = "success"
            return JsonResponse(result)
        else:
            result["data"] = "Please login and then access the link."
            return JsonResponse(result)
    else:
        result["data"] = "request error"
    return JsonResponse(result)









