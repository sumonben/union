import os
from django.db import models
from django.urls import reverse
from payment.models import Transaction
from django.utils.html import format_html
from django.template.defaultfilters import escape
from region.models import District,Division,Upazilla,Union,PostOffice,Village,Ward,Mouja,OthersAdress
from certificate.models import Adress
from account.models import Member,Chairman
from ckeditor.fields import RichTextField
from django.dispatch import receiver
# Create your models here.

class FiscalYear(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=100,unique=True,blank=True,null=True)
    title_en=models.CharField(max_length=100,unique=True,blank=True,null=True)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title_en

class HoldingType(models.Model):
    serial=models.IntegerField(default=10,verbose_name="ক্রম")
    name=models.CharField(max_length=500,verbose_name=" নাম(বাংলায়)")
    name_en=models.CharField(max_length=500,verbose_name=" নাম(ইংরেজিতে)")
    amount=models.IntegerField(default=10)
    template=models.CharField(max_length=250,blank=True,null=True)
    image=models.ImageField(upload_to='media/',blank=True,null=True,)
    is_active=models.BooleanField(default=False,verbose_name="সক্রিয় কিনা?")
    is_auto_sign=models.BooleanField(default=False)
    is_join_sign=models.BooleanField(default=False)
    class Meta:
        ordering = ['serial']
        verbose_name="হোল্ডিং টেক্সের ধরণ"
        verbose_name_plural="হোল্ডিং টেক্সের ধরণসমূহ"
    def __str__(self):
        return self.name+'('+self.name_en+')'
class HoldingTax(models.Model):
    serial=models.IntegerField(default=10,verbose_name="ক্রম")
    holding_no=models.CharField(max_length=500,verbose_name=" হোল্ডিং নাম্বার(ইংরেজিতে)")
    name=models.CharField(max_length=500,blank=True,null=True,verbose_name=" নাম(বাংলায়)")
    name_en=models.CharField(max_length=500,blank=True,null=True,verbose_name=" নাম(ইংরেজিতে)")
    email=models.EmailField(max_length=100,blank=True,null=True,verbose_name="ইমেইল(যদি থাকে)")
    phone=models.CharField(max_length=11,blank=True,null=True,verbose_name="মোবাইল নং")
    nid=models.CharField(max_length=17,null=True,blank=True,verbose_name="জাতীয় পরিচপত্র")
    father_name=models.CharField(max_length=500,blank=True,null=True,verbose_name="বাবার নাম(বাংলায়)")
    father_name_en=models.CharField(max_length=500,blank=True, null=True,verbose_name="বাবার নাম(ইংরেজিতে)")
    mother_name=models.CharField(max_length=500,blank=True,null=True,verbose_name="মায়ের নাম(বাংলায়)")
    mother_name_en=models.CharField(max_length=500,blank=True, null=True,verbose_name="মায়ের নাম(ইংরেজিতে)")
    adress=models.ForeignKey(Adress,null=True, blank=True,on_delete=models.SET_NULL,verbose_name="ঠিকানা")
    village=models.ForeignKey(Village,null=True, blank=True,on_delete=models.SET_NULL,verbose_name="গ্রাম/মহল্লা")
    ward=models.ForeignKey(Ward,null=True, blank=True,on_delete=models.SET_NULL,verbose_name="ওয়ার্ড")
    post_office=models.ForeignKey(PostOffice,null=True, blank=True,on_delete=models.SET_NULL,verbose_name="পোস্ট-অফিস")
    holding_type=models.ForeignKey(HoldingType,blank=True,null=True,on_delete=models.SET_NULL)
    amount=models.IntegerField(blank=True,null=True,verbose_name="পরিমান(টাকায়)")
    fiscal_year=models.ForeignKey(FiscalYear,null=True, blank=True,on_delete=models.SET_NULL,verbose_name="টেক্সের বছর")
    is_paid=models.BooleanField(default=False,verbose_name="প্রদানকৃত কিনা?")
    transaction=models.ForeignKey(Transaction,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="ট্রান্সেকশন")
    class Meta:
        ordering = ['serial']
        verbose_name="হোল্ডিং টেক্স"
        verbose_name_plural="হোল্ডিং টেক্সসমূহ"
    def __str__(self):
        if self.name and self.name_en:
            return self.name+'('+self.name_en+')'
        else:
            return str(self.id)