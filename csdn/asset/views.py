#coding:utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
import platform,xlrd,xlwt,os,datetime
from User.forms import Register
from User.models import CMDBUser
from models import *


def filepath():
    if 'Windows' in platform.system():
        p = os.getcwd() + "\static\uploadfile"
        return p
    elif 'Linux' in platform.system():
        p = os.getcwd() + "/static/uploadfile"
        return p

# 资产首页
def index(request):
    pass

# 桌面资产
def desktop(request):
    register = Register()
    listdata = Desktops.objects.all()
    return render(request,'asset/desktop.html',locals())


#检查SN是否重复
def valid_sn(sn):
    try:
        sn = Desktops.objects.get(sn=sn)
    except:
        return sn
    else:
        return "该设备编码已经被注册！"

def sn_valid(request):
    result = {"type": "error", "data": ""}
    if request.method == "GET":
        sn = request.GET["sn"]
        res = valid_sn(sn)
        if sn == res:
            result["type"] = "success"
            result["data"] = res
        else:
            result["type"] = "error"
            result["data"] = res
    else:
        result["data"] = "request must be get"
    return JsonResponse(result)


# 添加设备
def desktop_register(request):
    result = {"type":"error","data":""}
    if request.method == "POST":
        desktop = Desktops()
        desktop.sn = request.POST["sn"]
        desktop.name = request.POST["name"]
        desktop.brand = request.POST["brand"]
        desktop.number = request.POST["number"]
        desktop.type = request.POST["type"]
        desktop.department = request.POST["department"]
        desktop.user = request.POST["user"]
        desktop.statue = request.POST["statue"]
        desktop.location = request.POST["location"]
        desktop.delivery_time = request.POST["delivery_time"]
        desktop.remark = request.POST["remark"]
        desktop.save()
        result["type"] = "success"
        result["data"] = "success"
    else:
        result["data"] = "request must be post"
    return JsonResponse(result)


def desktop_info(request,sid):
    id = int(sid)
    result = {"type":"error","data":""}
    if request.method == "GET":
        try:
            username = request.session.get("username")
            user = CMDBUser.objects.get(username=username)
        except:
            result["data"] = "you are must login"
            return JsonResponse(result)
        else:
            d_data = Desktops.objects.get(id = id)
            result["type"] = "success"
            result["data"] = {
                "sn": d_data.sn,
                "name": d_data.name,
                "brand": d_data.brand,
                "number": d_data.number,
                "type": d_data.type,
                "department": d_data.department,
                "user": d_data.user,
                "statue": d_data.statue,
                "location": d_data.location,
                "delivery_time": d_data.delivery_time,
                "remark": d_data.remark,
            }

    elif request.method == "POST" and request.POST:
        print id,type(id)
        print request.POST["sn"]
        Desktops.objects.filter(id=id).update(
            sn = request.POST["sn"],
            name = request.POST["name"],
            brand = request.POST["brand"],
            number = request.POST["number"],
            type = request.POST["type"],
            department = request.POST["department"],
            user = request.POST["user"],
            statue = request.POST["statue"],
            location = request.POST["location"],
            delivery_time = request.POST["delivery_time"],
            remark = request.POST["remark"]
        )
        print request.POST["sn"]
        return redirect("/asset/desktop")
    else:
        return render(request, "asset/desktopinfo.html", locals())
    return render(request,"asset/desktopinfo.html",locals())


# 上传excel导入到数据库里
def desktops_upload_file(request):
    path = filepath()
    if request.method == 'POST':
        file_obj = request.FILES.get('file')
        # 判断选择文件
        if file_obj:
            filename = os.path.join(path,file_obj.name)
            filetype = str(os.path.splitext(filename)[1])
            # 判断文件类型
            if filetype == ".xls":
                # 判断文件是否重名或者是否已经存在
                if os.path.exists(filename):
                    result = {"statue": "error", "data": "文件已经存在！！！"}
                    return JsonResponse(result)
                else:
                    # 把上传过来的文件保存
                    excelfile = open(filename,'wb+')
                    for filedata in file_obj.chunks():
                        excelfile.write(filedata)
                        excelfile.close()
                    # 打开上传过来的excel文件
                    excel = xlrd.open_workbook(filename)
                    # 获取所有sheet名字
                    # sheet_len = len(excel.sheet_names())
                    # 遍历出第一个的sheet内容，然后进行处理
                    sheets = excel.sheet_by_index(0)
                    rows_len = sheets.nrows
                    print rows_len
                    cols_len = sheets.ncols
                    print cols_len
                    # print sheets.name,sheets.nrows,sheets.ncols
                    # 获取有多少行sheets.nrows,
                    # 获取有多少列sheets.ncols
                    for r in range(1,rows_len):
                            r_data = sheets.row_values(r)
                            print r_data[0]
                            # print r_data
                            d = Desktops()
                            d.sn = r_data[0]
                            d.name = r_data[1]
                            d.brand = r_data[2]
                            d.number = r_data[3]
                            d.type = r_data[4]
                            d.department = r_data[5]
                            d.user = r_data[6]
                            d.statue = r_data[7]
                            d.location = r_data[8]
                            d.delivery_time = r_data[9]
                            d.remark = r_data[10]
                            d.save()
                    # print excel.sheet_by_index(1)
                result = {"statue": "success","data":"数据导入成功成功！！！"}
                return JsonResponse(result)
            else:
                result = {"statue": "error", "data": "文件格式不对，必须是:xlsx"}
                return JsonResponse(result)
        else:
            result = {"statue": "error", "data": "你没有选择文件呢！！！"}
            return JsonResponse(result)

    result = {"statue": "error","data": "你没有选择文件呢！！！"}
    return JsonResponse(result)

# 下载服务器上的excel模板到本地
def desktops_downlload_excelmodels(request):
    # 打开一个新的excel文件
    c_name = xlwt.Workbook(encoding='utf8')
    # 创建一个sheet
    c_sheet = c_name.add_sheet('sheet')
    # 打开服务器上的excel模板文件
    path = filepath()
    s_name = os.path.join(path, "desktops_models.xlsx")
    excel = xlrd.open_workbook(s_name)
    sheets = excel.sheet_by_index(0)
    rows_len = sheets.nrows
    cols_len = sheets.ncols
    # print sheets.name,sheets.nrows,sheets.ncols
    # 获取有多少行sheets.nrows,
    # 获取有多少列sheets.ncols

    # 获取第0行的值
    r_data = sheets.row_values(0)
    for i in range(cols_len):
        c_sheet.write(0,i,r_data[i])
    nowdate = datetime.datetime.now().strftime('%Y-%m-%d')
    response = HttpResponse(content_type='application/msexcel')
    response['Content-Disposition'] = 'attachment; filename=%s_models.xls'%nowdate

    c_name.save(response)

    return response

# 下载桌面PC所有数据
def desktops_download_alldata(request):

    # 打开一个新的excel文件
    excel = xlwt.Workbook(encoding='utf8')
    # 创建一个sheet
    sheet = excel.add_sheet('sheet')
    # 获取表有多少条数据
    #           行 列   值
    sheet.write(0, 0, '设备编码')
    sheet.write(0, 1, '设备名称')
    sheet.write(0, 2, '品牌')
    sheet.write(0, 3, '数量')
    sheet.write(0, 4, '型号')
    sheet.write(0, 5, '部门')
    sheet.write(0, 6, '使用人')
    sheet.write(0, 7, '状态')
    sheet.write(0, 8, '所在位置')
    sheet.write(0, 9, '出厂时间')
    sheet.write(0, 10, '备注')
    len_d = Desktops.objects.count()
    for i in range(1,len_d+1):
        D_data = Desktops.objects.filter(id = i)
        for s_data in D_data:
            sheet.write(i,0,s_data.sn)
            sheet.write(i,1,s_data.name)
            sheet.write(i,2,s_data.brand)
            sheet.write(i,3,s_data.number)
            sheet.write(i,4,s_data.type)
            sheet.write(i,5,s_data.department)
            sheet.write(i,6,s_data.user)
            sheet.write(i,7,s_data.statue)
            sheet.write(i,8,s_data.location)
            sheet.write(i,9,s_data.delivery_time)
            sheet.write(i,10,s_data.remark)
    nowdate = datetime.datetime.now().strftime('%Y-%m-%d')
    response = HttpResponse(content_type='application/msexcel')
    response['Content-Disposition'] = 'attachment; filename=%s.xls'%nowdate
    excel.save(response)
    return response