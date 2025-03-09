from django.db import models
from django.urls import reverse
from payment.models import Transaction
from django.utils.html import format_html
from django.template.defaultfilters import escape
from region.models import District,Division,Upazilla,Union,PostOffice,Village,Ward,Mouja
from account.models import Member,Chairman
#from account.models import UserModel
# Create your models here.



class Relation(models.Model):
    serial=models.IntegerField(default=10,verbose_name="ক্রম")
    name=models.CharField(max_length=500,verbose_name=" নাম(বাংলায়)")
    name_en=models.CharField(max_length=500,verbose_name=" নাম(ইংরেজিতে)")
    class Meta:
        ordering = ['serial']
        verbose_name="সম্পর্ক"
        verbose_name_plural="সম্পর্ক"
    def __str__(self):
        return self.name+'('+self.name_en+')'

class Person(models.Model):
    serial=models.IntegerField(default=10)
    name=models.CharField(max_length=500,verbose_name=" নাম(বাংলায়)")
    name_en=models.CharField(max_length=500,verbose_name=" নাম(ইংরেজিতে)")
    relation=models.ForeignKey(Relation,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="সম্পর্ক")
    comment=models.CharField(max_length=500,blank=True,null=True,verbose_name="মন্তব্য")

    class Meta:
        ordering = ['serial']
        verbose_name=" ওয়ারিশ"
        verbose_name_plural=" ওয়ারিশগণ"
    def __str__(self):
        return self.name+'('+self.name_en+')'

class Cause(models.Model):
    serial=models.IntegerField(default=10)
    name=models.CharField(max_length=500,verbose_name=" নাম(বাংলায়)")
    name_en=models.CharField(max_length=500,verbose_name=" নাম(ইংরেজিতে)")
    class Meta:
        ordering = ['serial']
        verbose_name="কারণ"
        verbose_name_plural="কারণ"
    def __str__(self):
        return self.name+'('+self.name_en+')'

class CertificateType(models.Model):
    serial=models.IntegerField(default=10)
    name=models.CharField(max_length=250)
    name_en=models.CharField(max_length=250)
    amount=models.IntegerField(default=10)
    image=models.ImageField(upload_to='media/',blank=True,null=True,)
    is_active=models.BooleanField(default=False)
    class Meta:
        ordering = ['name_en']
        verbose_name=" সনদের ধরণ"
        verbose_name_plural=" সনদের ধরণ"
    def __str__(self):
        return self.name+'('+self.name_en+')'


class Adress(models.Model):
    serial=models.IntegerField(default=10)
    holding_no=models.CharField(max_length=50,blank=True,null=True,verbose_name=" হোল্ডিং নং")
    ward=models.ForeignKey(Ward,on_delete=models.SET_NULL,blank=True,null=True,verbose_name="ওয়ার্ড নং ")
    mouja=models.ForeignKey(Mouja,on_delete=models.SET_NULL,blank=True,null=True,verbose_name="মৌজা")
    village=models.ForeignKey(Village,on_delete=models.SET_NULL,blank=True,null=True,verbose_name=" গ্রাম/মহল্লা")
    post_office=models.ForeignKey(PostOffice,on_delete=models.SET_NULL,blank=True,null=True,verbose_name="ডাকঘর ")
    district=models.ForeignKey(District,blank=True,null=True,on_delete=models.SET_NULL,verbose_name=" জেলা ")
    upazilla=models.ForeignKey(Upazilla,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="উপজেলা ")
    union=models.ForeignKey(Union,blank=True,null=True,on_delete=models.SET_NULL,verbose_name=" ইউনিয়ন ")

    class Meta:
        ordering = ['serial']
        verbose_name="ঠিকানা"
        verbose_name_plural="ঠিকানা"
    def __str__(self):
        if self.village:
            return self.village.name
        else:
            return '1'


class Certificate(models.Model):
    name=models.CharField(max_length=500,verbose_name="নাম(বাংলায়)")
    name_en=models.CharField(max_length=500,blank=True, null=True,verbose_name="নাম (ইংরেজিতে)")
    email=models.EmailField(max_length=100,blank=True,null=True,verbose_name="ইমেইল(যদি থাকে)")
    phone=models.CharField(max_length=11,blank=True,null=True,verbose_name="মোবাইল নং")
    nid=models.CharField(max_length=17,null=True,blank=True,verbose_name="জাতীয় পরিচপত্র")
    passport=models.CharField(max_length=17,null=True,blank=True,verbose_name="পাসপোর্ট নং")
    father_name=models.CharField(max_length=500,verbose_name="বাবার নাম(বাংলায়)")
    father_name_en=models.CharField(max_length=500,blank=True, null=True,verbose_name="বাবার নাম(ইংরেজিতে)")
    mother_name=models.CharField(max_length=500,verbose_name="মায়ের নাম(বাংলায়)")
    mother_name_en=models.CharField(max_length=500,blank=True, null=True,verbose_name="মায়ের নাম(ইংরেজিতে)")
    dob=models.DateField(null=True,blank=True)
    adress=models.ForeignKey(Adress,null=True, blank=True,on_delete=models.SET_NULL,verbose_name="ঠিকানা")
    description=models.TextField(max_length=1000,null=True,blank=True,verbose_name="কারণ বর্ণনাঃ")
    cause=models.ForeignKey(Cause,on_delete=models.SET_NULL,blank=True, null=True,verbose_name="কারণঃ")
    caste=models.CharField(max_length=500,blank=True, null=True,verbose_name="সম্প্রদায়")
    profession=models.CharField(max_length=500,blank=True, null=True,verbose_name="পেশা")
    income=models.IntegerField(null=True,blank=True,verbose_name="আয়")
    amount=models.CharField(max_length=10,null=True,blank=True,verbose_name="পরিমাণ")
    date = models.DateField(null=True,blank=True)
    file=models.FileField(upload_to='media/',blank=True,null=True,verbose_name="মেম্বারের সুপারিশ ফাইল")
    nid_file=models.FileField(upload_to='media/',blank=True,null=True,verbose_name="এনআইডি-জন্ম নিবন্ধন")
    transaction=models.ForeignKey(Transaction,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="ট্রান্সেকশন")
    certificate_type=models.ForeignKey(CertificateType,on_delete=models.SET_NULL,null=True, blank=True,verbose_name="সনদের ধরণ")
    person=models.ManyToManyField(Person,blank=True,verbose_name="ওয়ারিশগণ")
    tracking_no=models.CharField(max_length=25,null=True, blank=True,verbose_name="ট্র্যাকিং নং")
    is_verified=models.BooleanField(default=False,verbose_name="ভেরিফাইড কিনা?")
    chairman=models.ForeignKey(Chairman,on_delete=models.SET_NULL,blank=True,null=True,verbose_name="চেয়ারম্যান")
    member=models.ForeignKey(Member,on_delete=models.SET_NULL,blank=True,null=True,verbose_name="সদস্য")
    language=models.CharField(max_length=250,blank=True,null=True,verbose_name="ভাষা")
    
    class Meta:
        verbose_name="সনদসমূহ"
        verbose_name_plural="সনদসমূহ"

    def __str__(self):
        return self.name +':'+ str(self.phone)
   
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

# class WarishanCertificate(models.Model):
#     name=models.CharField(max_length=100,verbose_name="নাম(বাংলায়)")
#     name_en=models.CharField(max_length=100,blank=True, null=True,verbose_name="নাম (ইংরেজিতে)")
#     email=models.EmailField(max_length=50,blank=True,null=True,verbose_name="ইমেইল(যদি থাকে)")
#     phone=models.CharField(max_length=11,blank=True,null=True,verbose_name="মোবাইল নং")
#     nid=models.CharField(max_length=17,null=True,blank=True,verbose_name="জাতীয় পরিচপত্র")
#     father_name=models.CharField(max_length=100,verbose_name="বাবার নাম(বাংলায়)")
#     father_name_en=models.CharField(max_length=100,blank=True, null=True,verbose_name="বাবার নাম(ইংরেজিতে)")
#     mother_name=models.CharField(max_length=100,verbose_name="মায়ের নাম(বাংলায়)")
#     mother_name_en=models.CharField(max_length=100,blank=True, null=True,verbose_name="মায়ের নাম(ইংরেজিতে)")
#     adress=models.ForeignKey(Adress,null=True, blank=True,on_delete=models.SET_NULL,verbose_name="ঠিকানা")
#     cause=models.ForeignKey(Cause,on_delete=models.SET_NULL,blank=True, null=True,verbose_name="কারণঃ")
#     file=models.FileField(upload_to='media/',blank=True,null=True,verbose_name="মেম্বারের সুপারিশ ফাইল")
#     nid_file=models.FileField(upload_to='media/',blank=True,null=True,verbose_name="এনআইডি-জন্ম নিবন্ধন")
#     transaction=models.ForeignKey(Transaction,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="ট্রান্সেকশন")
#     certificate_type=models.ForeignKey(CertificateType,on_delete=models.SET_NULL,null=True, blank=True,verbose_name="সনদের ধরণ")
#     person=models.ManyToManyField(Person,blank=True,verbose_name="ওয়ারিশগণ")
#     tracking_no=models.CharField(max_length=25,null=True, blank=True,verbose_name="ট্র্যাকিং নং")
#     is_verified=models.BooleanField(default=False,verbose_name="ভেরিফাইড কিনা?")
#     language=models.CharField(max_length=25,blank=True,null=True,verbose_name="ভাষা")
#     class Meta:
#         verbose_name="ওয়ারিশান সনদ"
#         verbose_name_plural="ওয়ারিশান সনদ"

#     def __str__(self):
#         return self.name +':'+ self.phone
   
#     def __unicode__(self):
#         return self.name_bangla
#     def amount_paid(self):
#         tran=self.transaction
#         if tran:
#             return  tran.amount
#     def transaction_detaills(self):
#         tran=self.transaction
#         if tran:
#             return format_html('<a href="%s" target="_blank">%s</a>' % (reverse("admin:payment_transaction_change", args=(tran.id,)) , escape(tran.tran_id)))
     
#     def paid_at(self):
#         tran=self.transaction
#         if tran:
#             return  tran.created_at
