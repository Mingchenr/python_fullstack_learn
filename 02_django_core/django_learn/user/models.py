from djamgo.db import models

class User(models.Model):
    name = models.CharField(max_length=50,verbose_name="用户名")
    age = models.IntegerField(verbose_name = "年龄",null=True,blank=True)
    create_time = models.DaateTimeField(auto_now_add = True,verbose_name= "创建时间")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户列表"
