"""
Task下的表　用于task管理
20210302
"""

from django.db import models


# Create your models here.
from user.models import User


class Task(models.Model):
    tid = models.AutoField('任务id',primary_key=True)
    #外键User.uid
    inier = models.ForeignKey(User,verbose_name='发布人', related_name="inier", on_delete=models.CASCADE,null=False)
    accer = models.ForeignKey(User, verbose_name='接受人',related_name="accer",on_delete=models.CASCADE,null=True)
    #content=models.ForeignKey()
    #参考数据库文档修改price
    price= models.IntegerField('任务赏金',default=0)


    #参考数据库文档修改 task_status
    task_status=models.CharField(max_length=2,default='00')

    reated_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)



class Task_contents(models.Model):
    #一对一　Task.tid
    content=models.OneToOneField(Task,on_delete=models.CASCADE,primary_key=True)
    task_title=models.CharField("任务主题",max_length=64,null=False)
    text=models.TextField('文字内容',max_length=1280,null=False)

    #pic通过上传文件中的orm方式储存，字段中自动保存文件路径
    #目前未测试
    pic = models.ImageField('图片内容', upload_to='task_pic',null=True)

class Task_wantget(models.Model):
     # 一对一　Task.tid
     task = models.OneToOneField(Task, on_delete=models.CASCADE, primary_key=True)
     # 外键User.uid
     wgeter =models.ForeignKey(User, verbose_name='学生们',on_delete=models.CASCADE,null=True)






"""
测试数据请在dj　shell中插入

u1= User.objects.get(uid=1)
Task.objects.create(inier=u1)



t1=Task.objects.get(tid=1)
c1=Task_contents.objects.create(content=t1,
                        task_title="测试文本主题",
                        text='测试文本内容',)
                        
               
       
w1=Task_wantget.objects.create(task=t1,
                            wgeter=u1,
                   )                 
                    
"""
