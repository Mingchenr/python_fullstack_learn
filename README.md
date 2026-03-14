# python全栈学习笔记（第1周）
## 🔥 学习目标
掌握Python基础、函数进阶、面向对象、常用库（resquests/payhlib）、Git版本管理

## 📂 包含项目
|  文件名 |  功能说明|
|---------|-----------|
| day1_basic.py |  Python基础语法（变量/循环/列表）|
| day2_decorator.py | 权限验证装饰器实战|
| day3_oop_student.py | 学生管理系统（面向对象/封装/继承/多态）|
| day4_crawl_rename.py | 壁纸爬虫  + 文件批量重命名 + POST 接口测试 |


## 🛠️  技术栈

Python 3.10+ |  requests |  lxml |  pathlib  | Git |

## 🚀 运行说明
### 1. 壁纸爬虫（需安装依赖）
```bash
# 安装依赖
pip install requests lxml
# 运行爬虫
python day4_crawl_rename.py



"""
核心代码复盘
"""
# 1.装饰器
#带参数的权限装饰器
def permission_required(role = "admin"):
    def decorator(func):
        def wrapper(*args,**kwargs):
            user_role = input("请输入角色：")

            if user_role != role :
                print("无权限")
                return
            return  func(*args,**kwargs)
        return wrapper
    return decorator

@ permission_required(role="admin")

def admin_op():
    print("管理员操作执行")

admin_op()



#requests POST请求（DRF接口基础）
import requests
import json

url = "https://httpbin.org/post"
data = {"name":"王康","age":33}
headers = {"Content-type":"application/json"}

response = requests.post(url,json=data,headers=headers)
print(json.dumps(response.json()["json"],ensure_ascii=False,indent = 2))

#Django项目创建核心命令

django-admin startproject myproject
cd myproject
python manage.py ruserver

#Vue项目创建核心命令

vue create muvue
cd myvue
npm run serve

