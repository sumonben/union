from django.db import models
from django.urls import reverse
from payment.models import Transaction
from django.utils.html import format_html
from django.template.defaultfilters import escape
#from account.models import UserModel
# Create your models here.


class Division(models.Model):
    name=models.CharField(max_length=25,unique=True)
    name_en=models.CharField(max_length=15,unique=True)
    link=models.CharField(max_length=15,null=True,blank=True)
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name+'('+self.name_en+')'

class District(models.Model):
    name=models.CharField(max_length=25,unique=True)
    name_en=models.CharField(max_length=25,unique=True)
    lattitude=models.CharField(max_length=15,blank=True,null=True)
    longitude=models.CharField(max_length=15, blank=True,null=True)
    division=models.ForeignKey(Division, on_delete=models.CASCADE,blank=True,null=True)
    link=models.CharField(max_length=15,null=True,blank=True)
    class Meta:
        ordering = ['name_en']
    def __str__(self):
        return self.name+'('+self.name_en+')'

class Upazilla(models.Model):
    name=models.CharField(max_length=25)
    name_en=models.CharField(max_length=25)
    district=models.ForeignKey(District, on_delete=models.CASCADE,blank=True,null=True)
    link=models.CharField(max_length=15,null=True,blank=True)
    class Meta:
        ordering = ['name_en']
    def __str__(self):
        return self.name+'('+self.name_en+')'

class Union(models.Model):
    name=models.CharField(max_length=25)
    name_en=models.CharField(max_length=25)
    upazilla=models.ForeignKey(Upazilla, on_delete=models.CASCADE,blank=True,null=True)
    link=models.CharField(max_length=15,null=True,blank=True)

    class Meta:
        ordering = ['name_en']
    def __str__(self):
        return self.name+'('+self.name_en+')'

class Relation(models.Model):
    serial=models.IntegerField(default=10)
    name=models.CharField(max_length=25)
    name_en=models.CharField(max_length=25)
    class Meta:
        ordering = ['name_en']
    def __str__(self):
        return self.name+'('+self.name_en+')'

class Warish(models.Model):
    serial=models.IntegerField(default=10)
    name=models.CharField(max_length=25)
    name_en=models.CharField(max_length=25)
    relation=models.ForeignKey(Relation,blank=True,null=True,on_delete=models.SET_NULL)

    class Meta:
        ordering = ['name_en']
    def __str__(self):
        return self.name+'('+self.name_en+')'


class CertificateType(models.Model):
    serial=models.IntegerField(default=10)
    name=models.CharField(max_length=25)
    name_en=models.CharField(max_length=25)
    class Meta:
        ordering = ['name_en']
    def __str__(self):
        return self.name+'('+self.name_en+')'


class Adress(models.Model):
    serial=models.IntegerField(default=10)
    holding_no=models.CharField(max_length=50,blank=True,null=True)
    village=models.CharField(max_length=50,blank=True,null=True)
    word_no=models.CharField(max_length=25,blank=True,null=True)
    post_office=models.CharField(max_length=25,blank=True,null=True)
    district=models.ForeignKey(District,blank=True,null=True,on_delete=models.SET_NULL)
    upazilla=models.ForeignKey(Upazilla,blank=True,null=True,on_delete=models.SET_NULL)
    union=models.ForeignKey(Union,blank=True,null=True,on_delete=models.SET_NULL)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        if self.village_or_house:
            return self.village_or_house
        else:
            return '1'


class Certificate(models.Model):
    name=models.CharField(max_length=100)
    name_bangla=models.CharField(max_length=100,blank=True, null=True)
    email=models.EmailField(max_length=50,blank=True,null=True)
    phone=models.CharField(max_length=11,blank=True,null=True)
    nid=models.CharField(max_length=17,blank=True,null=True)
    father_name=models.CharField(max_length=100)
    father_name_en=models.CharField(max_length=100,blank=True, null=True)
    mother_name=models.CharField(max_length=100)
    mother_name_en=models.CharField(max_length=100,blank=True, null=True)
    adress=models.ForeignKey(Adress,null=True, blank=True,on_delete=models.SET_NULL)
    transaction=models.ForeignKey(Transaction,blank=True,null=True,on_delete=models.SET_NULL)
    certificate_type=models.CharField(max_length=15,null=True, blank=True,)
    tracking_no=models.CharField(max_length=25,null=True, blank=True,)
    is_verified=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name +':'+ self.phone
   
    def __unicode__(self):
        return self.name_bangla
    def amount_paid(self):
        tran=self.transaction
        if tran:
            return  tran.amount
    def transaction_detaills(self):
        tran=self.transaction
        if tran:
            return format_html('<a href="%s" target="_blank">%s</a>' % (reverse("admin:payment_transaction_change", args=(tran.id,)) , escape(tran.tran_id)))
     
    def paid_at(self):
        tran=self.transaction
        if tran:
            return  tran.created_at

class WarishanCertificate(models.Model):
    name=models.CharField(max_length=100,verbose_name="নাম(বাংলায়)")
    name_en=models.CharField(max_length=100,blank=True, null=True,verbose_name="নাম (ইংরেজিতে)")
    email=models.EmailField(max_length=50,blank=True,null=True,verbose_name="ইমেইল(যদি থাকে)")
    phone=models.CharField(max_length=11,blank=True,null=True,verbose_name="মোবাইল নং")
    nid=models.CharField(max_length=17,null=True,blank=True,verbose_name="জাতীয় পরিচপত্র")
    father_name=models.CharField(max_length=100,verbose_name="বাবার নাম")
    father_name_en=models.CharField(max_length=100,blank=True, null=True,verbose_name="বাবার নাম(ইংরেজিতে)")
    mother_name=models.CharField(max_length=100,verbose_name="মায়ের নাম(বাংলায়)")
    mother_name_en=models.CharField(max_length=100,blank=True, null=True,verbose_name="মায়ের নাম(ইংরেজিতে)")
    adress=models.ForeignKey(Adress,null=True, blank=True,on_delete=models.SET_NULL,verbose_name="ঠিকানা")
    transaction=models.ForeignKey(Transaction,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="ট্রান্সেকশন")
    certificate_type=models.CharField(max_length=15,null=True, blank=True,verbose_name="সনদের ধরণ")
    warish=models.ManyToManyField(Warish,blank=True,verbose_name="ওয়ারিশগণ")
    tracking_no=models.CharField(max_length=25,null=True, blank=True,verbose_name="ট্র্যাকিং নং")
    is_verified=models.BooleanField(default=False,verbose_name="ভেরিফাইড কিনা?")
    
    class Meta:
        verbose_name="ওয়ারিশান সনদ"
        verbose_name_plural="ওয়ারিশান সনদ"

    def __str__(self):
        return self.name +':'+ self.phone
   
    def __unicode__(self):
        return self.name_bangla
    def amount_paid(self):
        tran=self.transaction
        if tran:
            return  tran.amount
    def transaction_detaills(self):
        tran=self.transaction
        if tran:
            return format_html('<a href="%s" target="_blank">%s</a>' % (reverse("admin:payment_transaction_change", args=(tran.id,)) , escape(tran.tran_id)))
     
    def paid_at(self):
        tran=self.transaction
        if tran:
            return  tran.created_at
