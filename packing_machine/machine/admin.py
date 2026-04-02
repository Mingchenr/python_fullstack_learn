from django.contrib import admin
from .models import PackingMachine


# Register your models here.


@admin.register(PackingMachine)
class PackingMachineAdmin(admin.ModelAdmin):
    list_display = ("material_code", 'drawing_no', 'machine_name', 'selling_price', 'model_type')

    #可搜索字段
    search_fields = ('material_code', 'machine_name')

    #过滤器
    list_filter = ('model_type',)

    #只读字段
    readonly_fields = ('created_at', 'updated_at')

    # 编辑页面字段分组
    fieldset = (
        ('基础信息', {
            'fields': ('material_code', 'drawing_no', 'machine_name', 'selling_price', 'model_type')
        }),
        ('媒体信息', {
            'fields': ('image',)
        }),
        ('时间信息', {
            'fields': ('created_at','updated_at'),
            'classes': ('collapse',)  #可折叠
        }),
    )
