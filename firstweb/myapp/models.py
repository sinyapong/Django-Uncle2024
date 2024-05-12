from django.db import models

class Tracking(models.Model):
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    tracking = models.CharField(max_length=100,null=True,blank=True)
    other = models.TextField(null=True,blank=True)

    def __str__(self):
        return f'{self.name} - {self.tel} ({self.tracking})'

class AskQa(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True,verbose_name='ชื่อผู้ติดต่อ')
    email = models.CharField(max_length=100,null=True,blank=True,verbose_name='อีเมล์')
    title = models.CharField(max_length=100,null=True,blank=True,verbose_name='หัวข้อ')
    detail = models.TextField(null=True,blank=True,verbose_name='รายละเอียด')

    def __str__(self):
        return f'{self.name}  {self.title}'