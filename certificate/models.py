import os
from django.db import models
from django.urls import reverse
from payment.models import Transaction
from django.utils.html import format_html
from django.template.defaultfilters import escape
from region.models import District,Division,Upazilla,Union,PostOffice,Village,Ward,Mouja,OthersAdress
from account.models import Member,Chairman
from ckeditor.fields import RichTextField
from django.dispatch import receiver
#from account.models import UserModel
# Create your models here.



class Gender(models.Model):
    serial=models.IntegerField(default=10,verbose_name="ক্রম")
    name=models.CharField(max_length=500,verbose_name=" নাম(বাংলায়)")
    name_en=models.CharField(max_length=500,verbose_name=" নাম(ইংরেজিতে)")
    class Meta:
        ordering = ['serial']
        verbose_name="লিঙ্গ"
        verbose_name_plural="লিঙ্গ"
    def __str__(self):
        return self.name+'('+self.name_en+')'
class MaritalStatus(models.Model):
    serial=models.IntegerField(default=10,verbose_name="ক্রম")
    name=models.CharField(max_length=500,verbose_name=" নাম(বাংলায়)")
    name_en=models.CharField(max_length=500,verbose_name=" নাম(ইংরেজিতে)")
    class Meta:
        ordering = ['serial']
        verbose_name="বৈবাহিক অবস্থা"
        verbose_name_plural="বৈবাহিক অবস্থা"
    def __str__(self):
        return self.name+'('+self.name_en+')'

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
    nid=models.CharField(max_length=17,null=True,blank=True,verbose_name="জাতীয় পরিচয়পত্র")
    dob=models.DateField(null=True,blank=True,verbose_name="জন্ম তারিখ")
    relation=models.ForeignKey(Relation,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="সম্পর্ক")
    phone=models.CharField(max_length=11,blank=True,null=True,verbose_name="মোবাইল নং")
    comment=models.CharField(max_length=500,blank=True,null=True,verbose_name="মন্তব্য")
    tracking_no=models.CharField(max_length=25,null=True, blank=True,verbose_name="ট্র্যাকিং নং")
    class Meta:
        ordering = ['serial']
        verbose_name="ব্যক্তি/ওয়ারিশগণ/অন্যান্য ব্যক্তিবর্গ"
        verbose_name_plural="ব্যক্তি/ওয়ারিশগণ/অন্যান্য ব্যক্তিবর্গ"
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
        return self.name

class CertificateType(models.Model):
    serial=models.IntegerField(default=10)
    name=models.CharField(max_length=250)
    name_en=models.CharField(max_length=250)
    amount=models.IntegerField(default=10)
    template=models.CharField(max_length=250,blank=True,null=True)
    image=models.ImageField(upload_to='media/',blank=True,null=True,)
    is_active=models.BooleanField(default=False)
    is_auto_sign=models.BooleanField(default=False)
    is_join_sign=models.BooleanField(default=False)
    main_body_bg=models.CharField(max_length=250,blank=True,null=True)
    header_bg=models.CharField(max_length=250,blank=True,null=True)
    title_bg=models.CharField(max_length=250,blank=True,null=True)
    body_bg=models.CharField(max_length=250,blank=True,null=True)
    heading_color=models.CharField(max_length=250,blank=True,null=True)
    subheading_color=models.CharField(max_length=250,blank=True,null=True)
    title_color=models.CharField(max_length=250,blank=True,null=True)

    class Meta:
        ordering = ['name']
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
        if self.village and self.ward and self.post_office:
            return self.ward.name+':'+self.village.name+':'+self.post_office.name
        elif self.village:
            return self.village.name+ ' : ' + self.ward.name
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
    memorial_no=models.CharField(max_length=500,blank=True, null=True,verbose_name="স্মারক নং")
    title=models.CharField(max_length=500,blank=True, null=True,verbose_name="বিবিধ")
    gender=models.ForeignKey(Gender,blank=True, null=True,on_delete=models.SET_NULL,verbose_name="লিঙ্গ")
    marital_status=models.ForeignKey(MaritalStatus,null=True, blank=True,on_delete=models.SET_NULL,verbose_name="বৈবাহিক অবস্থা")
    other_name=models.CharField(max_length=500,blank=True, null=True,verbose_name="স্বামীর নাম(বাংলায়)")
    other_name_en=models.CharField(max_length=500,blank=True, null=True,verbose_name="স্বামীর নাম(ইংরেজিতে)")
    dob=models.DateField(null=True,blank=True)
    adress=models.ForeignKey(Adress,null=True, blank=True,on_delete=models.SET_NULL,verbose_name="ঠিকানা")
    others_adress=models.ManyToManyField(OthersAdress, blank=True,verbose_name="অন্যান্য এলাকাভুক্ত ঠিকানা")
    description=RichTextField(null=True,blank=True,verbose_name="বর্ণনাঃ")
    cause=models.ForeignKey(Cause,on_delete=models.SET_NULL,blank=True, null=True,verbose_name="কারণঃ")
    caste=models.CharField(max_length=500,blank=True, null=True,verbose_name="সম্প্রদায়")
    profession=models.CharField(max_length=500,blank=True, null=True,verbose_name="পেশা")
    income=models.CharField(max_length=500,null=True,blank=True,verbose_name="আয়")
    amount=models.CharField(max_length=10,null=True,blank=True,verbose_name="পরিমাণ")
    date = models.DateField(null=True,blank=True)
    file=models.FileField(upload_to='media/member_file/%Y',blank=True,null=True,verbose_name="মেম্বারের সুপারিশ ফাইল")
    nid_file=models.FileField(upload_to='media/nid_file/%Y',blank=True,null=True,verbose_name="এনআইডি-জন্ম নিবন্ধন")
    transaction=models.ForeignKey(Transaction,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="ট্রান্সেকশন")
    certificate_type=models.ForeignKey(CertificateType,on_delete=models.SET_NULL,null=True, blank=True,verbose_name="সনদের ধরণ")
    person=models.ManyToManyField(Person,blank=True,verbose_name="ব্যক্তি/ওয়ারিশগণ/অন্যান্য ব্যক্তিবর্গ")
    tracking_no=models.CharField(max_length=25,null=True, blank=True,verbose_name="ট্র্যাকিং নং")
    is_verified=models.BooleanField(default=False,verbose_name="ভেরিফাইড কিনা?")
    comment=models.CharField(max_length=500,blank=True, null=True,verbose_name="মন্তব্য")
    chairman=models.ForeignKey(Chairman,on_delete=models.SET_NULL,blank=True,null=True,verbose_name="চেয়ারম্যান")
    member=models.ForeignKey(Member,on_delete=models.SET_NULL,blank=True,null=True,verbose_name="সদস্য")
    language=models.CharField(max_length=250,blank=True,null=True,verbose_name="ভাষা")
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    
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

    def delete(self, *args, **kwargs):
        if bool(self.nid_file) == True :
            os.remove(self.nid_file.path)
        if bool(self.file) == True:
            os.remove(self.file.path)
        for person in self.person.all():
            Person.objects.filter(id=person.id).delete()
        super(Certificate, self).delete(*args, **kwargs)

@receiver(models.signals.pre_save, sender=Certificate)
def auto_delete_file_on_change(sender, instance, **kwargs):
    
        if not instance.pk:
            return False

        try:
            old_file = Certificate.objects.get(pk=instance.pk).file
            old_nid_file = Certificate.objects.get(pk=instance.pk).nid_file

        except Certificate.DoesNotExist:
            return False

        new_file = instance.file
        if not old_file == new_file:
            if bool(old_file) == True:
                os.remove(old_file.path)

        new_file = instance.nid_file
        if not old_nid_file == new_file:
            if bool(old_nid_file) == True:
                os.remove(old_nid_file.path)

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
