from django.db import models
from region.models import Union,Word,Upazilla,District


# Create your models here.

class Post(models.Model):
    serial=models.IntegerField(default=10)
    name=models.CharField(max_length=25)
    name_en=models.CharField(max_length=25)
    class Meta:
        ordering = ['name_en']
        verbose_name="পদবী"
        verbose_name_plural="পদবী"

    def __str__(self):
        return self.name+'('+self.name_en+')'

class Chairman(models.Model):
    serial=models.IntegerField(default=10)
    name=models.CharField(max_length=25,verbose_name=" নাম(বাংলায়)")
    name_en=models.CharField(max_length=25,verbose_name=" নাম(ইংরেজিতে)")
    post=models.ForeignKey(Post,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="পদবী")
    union=models.ForeignKey(Union,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="ইউনিয়ন")
    upazilla=models.ForeignKey(Upazilla,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="উপজেলা")
    district=models.ForeignKey(District,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="জেলা")


    class Meta:
        ordering = ['serial']
        verbose_name="চেয়ারম্যান"
        verbose_name_plural="চেয়ারম্যান"
    def __str__(self):
        return self.name+'('+self.name_en+')'
class Member(models.Model):
    serial=models.IntegerField(default=10)
    name=models.CharField(max_length=25,verbose_name=" নাম(বাংলায়)")
    name_en=models.CharField(max_length=25,verbose_name=" নাম(ইংরেজিতে)")
    post=models.ForeignKey(Post,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="পদবী")
    word=models.ForeignKey(Word,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="ওয়ার্ড")
    union=models.ForeignKey(Union,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="ইউনিয়ন")
    upazilla=models.ForeignKey(Upazilla,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="উপজেলা")
    district=models.ForeignKey(District,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="জেলা")

    class Meta:
        ordering = ['serial']
        verbose_name="মেম্বার"
        verbose_name_plural="মেম্বার"
    def __str__(self):
        return self.name+'('+self.name_en+')'
