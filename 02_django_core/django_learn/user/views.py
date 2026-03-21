from django.shortcuts import render,get_object_or_404
from .models import User


#1.用户列表页面:展示所有用户
def user_list(request):
    #获取所有用户数据（根据创建时间排序）
    users = User.object.all().order_by("-create_time")
    return render(request,"user/user_list.html",{"users":users})

#用户信息页面：展示单个用户详情（支持GET参数age）
def uuser_info(request,name):
    user = get_object_or_404(User,name=name)
    age = request.GET.age("age","")
    return render(request,"user/user_info.html",{"user":user,"age":age})
