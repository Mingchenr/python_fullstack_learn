from os import name

from django.db import models
from time import time
import datetime

class SerialNumber:
    __current_date = "202140"
    __sequence_num = 0

    @classmethod
    def generate_serial_number(cls):
        cls.__sequence_num += 1

        serial_number = f"{cls.__current_date}{cls.__sequence_num:04d}"
        return serial_number


class PackingMachine(models.Model):
    """
    打包机
    """
    #1.物料编码
    material_code = models.CharField(
        max_length=20,
        primary_key=True,
        verbose_name='物料编码',
        help_text='唯一的物料编码',

    )

    #2.图号
    drawing_no = models.CharField(
        max_length=20,
        verbose_name="图号",
        help_text="示例图编号"
    )
    #3.规格
    standards = models.CharField(
        max_length=20,
        verbose_name="规格",
        help_text="M5*30"
    )

    #4.零件名称
    machine_name = models.CharField(
        max_length=100,
        verbose_name="零件名称",
        help_text="零件的中文名称",
    )


    #5.进货价格
    purchase_price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="价格",
        help_text="单位:元"
    )


    #6.卖价
    selling_price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="卖价",
        help_text="单位:元"
    )

    #7.图片路径
    image = models.ImageField(
        upload_to="machines/",
        null=True,
        blank=True,
        verbose_name="图片",
        help_text="零件图片文件",

    )

    #8.所属机型
    model_type = models.CharField(
        max_length=20,
        default="XQD-19",
        verbose_name="所属机型",
        choices=[
            ('XQD-19气动打包机','XQD-19气动打包机'),
            ('XQD-25气动打包机','XQD-25气动打包机'),
            ('GSC32气动打包机','GSC32气动打包机'),
            ('GSC32气动卡扣机','GSC32气动卡扣机'),
            ('KCL气动打包机','KCL气动打包机'),
            ('KCL气动卡扣机','KCL气动卡扣机'),
            ('FTL32气动打包机','FTL32气动打包机'),
            ('FTL32气动卡扣机','FTL32气动卡扣机'),

        ]
    )
    created_at=models.DateTimeField(
        auto_now_add=True,
        verbose_name = "创建时间"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="更新时间"
    )



    class Meta:
        verbose_name_plural = '气动打包机物料清单'
        ordering = ['material_code']


    def save(self,*args,**kwargs):
        if not self.material_code:
            self.material_code = SerialNumber.generate_serial_number()
        super().save(*args,**kwargs)

    def __str__(self):
        image_name = self.image.name if self.image else "无图片"
        return f"{self.material_code}-{self.machine_name}-{image_name}"


























