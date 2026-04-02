from django.urls import path

from . import views

app_name = "machine"

urlpatterns = [
    # 物料列表
    path('list/', views.machine_list, name='machine_list'),
    #物料详情
    path('detail/<str:code>/', views.machine_detail, name='machine_detail'),
    #添加物料
    path('add/', views.machine_add, name='machine_add'),
    #删除物料
    path('delete/<str:code>/', views.machine_delete, name='machine_delete'),
    path('edit/<str:code>/', views.machine_edit, name='machine_edit'),
]
