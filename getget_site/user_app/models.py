from django.db import models

# Create your models here.
from user.models import User


class User_profile(models.Model):
    #外键　User.uid
    user = models.ForeignKey(User, verbose_name='uid', on_delete=models.CASCADE, null=False)

    nickname= models.CharField('昵称', max_length=32)
    age = models.IntegerField('年龄',default=0)
    #1为男性
    sex = models.BooleanField('性别',blank=True,default=1)
    wallet = models.IntegerField('G币',default=0)
    #上传至mediam,未测试
    headpic = models.ImageField('照片', upload_to="headpic", blank=True, null=True)

    whatup = models.CharField('个性签名',max_length=32)
    uaddress = models.CharField('地址',max_length=64)
    #???
    #friends = PickledObjectField()# [groupid_uid:aliasname]
    lastonline_time=models.DateTimeField('最后上线时间',null=True)



class Message(models.Model):
    mid=models.AutoField('信息编号',primary_key=True)

    sender = models.ForeignKey(User,verbose_name='发信人',related_name="sender",on_delete=models.CASCADE,null=False)
    receiver = models.ForeignKey(User, verbose_name='收信人',related_name="receiver",on_delete=models.CASCADE,null=False)
    message=models.CharField("消息内容",max_length=128)
    #参考文档修改此字段
    message_status=models.CharField("消息状态",max_length=2)

class Web_nav(models.Model):
    # 外键　User.uid
    user = models.ForeignKey(User, verbose_name='uid', on_delete=models.CASCADE, null=False,primary_key=True)
    urls=models.CharField('网址收藏',max_length=128)


    """
    测试在DJ shell 中使用
    u1= User.objects.get(uid=1)
    
    User_profile.objects.create(user=u1,
                                wallet=1000,)

    
    """