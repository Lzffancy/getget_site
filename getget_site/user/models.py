"""
user下的表 用于验证用户的关键信息
20210302
"""


from django.db import models


# Create your models here.
class User(models.Model):
    uid=models.AutoField('用户id',primary_key=True)

    username = models.CharField('用户名', max_length=32)
    password=models.CharField('密码',max_length=32)
    email = models.EmailField('邮箱')
    phone = models.CharField('手机号码', max_length=11, default='')
    created_time=models.DateTimeField('创建时间',auto_now_add=True)
    updated_time=models.DateTimeField('更新时间',auto_now=True)

    #删除账号修改此字段　激活为1,删除为0
    active=models.BooleanField('激活状态',default=1)




"""
测试数据请在dj　shell中插入
 u2=User.objects.create(
   
                         username='tedu2',
                         password='123456',
                          email='123456@qq.com',
                           phone='15200536629',
                           )
                           
 u１=User.objects.create(
   
                         username='tedu1',
                         password='123456',
                          email='123456@qq.com',
                           phone='15200536629',
                           )                        
                           
                                      
"""

