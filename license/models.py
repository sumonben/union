from django.db import models
from django.urls import reverse
from payment.models import Transaction
from django.utils.html import format_html
from django.template.defaultfilters import escape
from region.models import District,Division,Upazilla,Union,PostOffice,Village,Ward,OthersAdress
from account.models import Member,Chairman,Secretary
from certificate.models import Adress,Person
from ckeditor.fields import RichTextField

# Create your models here.
class LicenseType(models.Model):
    serial=models.IntegerField(default=10)
    name=models.CharField(max_length=250)
    name_en=models.CharField(max_length=250)
    amount=models.IntegerField(default=10)
    template=models.CharField(max_length=250,blank=True,null=True)
    image=models.ImageField(upload_to='media/',blank=True,null=True,)
    is_active=models.BooleanField(default=False)
    class Meta:
        ordering = ['serial']
        verbose_name=" লাইসেন্স-এর ধরণ"
        verbose_name_plural=" লাইসেন্স-এর ধরণ"
    def __str__(self):
        return self.name+'('+self.name_en+')'




class License(models.Model):
    licensed_name=models.CharField(max_length=500,verbose_name="প্রতিষ্ঠানের নাম(বাংলায়)")
    licensed_name_en=models.CharField(max_length=500,blank=True, null=True,verbose_name="প্রতিষ্ঠানের নাম (ইংরেজিতে)")
    license_owner_name=models.CharField(max_length=500,verbose_name="লাইসেন্সধারীর নাম(বাংলায়)")
    license_owner_name_en=models.CharField(max_length=500,blank=True, null=True,verbose_name="লাইসেন্সধারীর নাম (ইংরেজিতে)")
    email=models.EmailField(max_length=100,blank=True,null=True,verbose_name="ইমেইল(যদি থাকে)")
    phone=models.CharField(max_length=11,blank=True,null=True,verbose_name="মোবাইল নং")
    nid=models.CharField(max_length=17,null=True,blank=True,verbose_name="জাতীয় পরিচপত্র")
    passport=models.CharField(max_length=17,null=True,blank=True,verbose_name="পাসপোর্ট নং (যদি থাকে)")
    father_name=models.CharField(max_length=500,verbose_name="বাবার নাম(বাংলায়)")
    father_name_en=models.CharField(max_length=500,blank=True, null=True,verbose_name="বাবার নাম(ইংরেজিতে)")
    mother_name=models.CharField(max_length=500,verbose_name="মায়ের নাম(বাংলায়)")
    mother_name_en=models.CharField(max_length=500,blank=True, null=True,verbose_name="মায়ের নাম(ইংরেজিতে)")
    adress=models.ForeignKey(OthersAdress,null=True, blank=True,on_delete=models.SET_NULL,verbose_name="ঠিকানা")
    adress_of_license=models.ForeignKey(Adress,related_name='adress_of_linsence',null=True, blank=True,on_delete=models.SET_NULL,verbose_name="প্রতিষ্ঠানের ঠিকানা")
    license_type=models.ForeignKey(LicenseType,on_delete=models.SET_NULL,null=True, blank=True,verbose_name="লাইসেন্সের ধরণ")
    license_no=models.CharField(max_length=500,blank=True, null=True,verbose_name="স্মারক নং")
    memorial_no=models.CharField(max_length=500,blank=True, null=True,verbose_name="স্মারক নং")
    person=models.ManyToManyField(Person,blank=True,verbose_name="অংশীদার গণ")
    description=RichTextField(max_length=1000,null=True,blank=True,verbose_name="কারণ বর্ণনাঃ")
    caste=models.CharField(max_length=500,blank=True, null=True,verbose_name="সম্প্রদায়")
    profession=models.CharField(max_length=500,blank=True, null=True,verbose_name="পেশা")
    capital=models.IntegerField(null=True,blank=True,verbose_name="পরিশোধিত মূলধন")    
    tax=models.IntegerField(null=True,blank=True,verbose_name="কর")
    fee=models.IntegerField(null=True,blank=True,verbose_name="ফি")
    vat_n_others=models.IntegerField(null=True,blank=True,verbose_name="ভ্যাট ও অন্যান্য")
    total_payment=models.IntegerField(null=True,blank=True,verbose_name="মোট প্রদেয়")
    total_payment_in_word=models.CharField(max_length=500,blank=True, null=True,verbose_name="মোট প্রদেয়(কথায়)")
    duration_form=models.DateField(blank=True, null=True)
    duration_to=models.DateField(blank=True, null=True)
    income=models.IntegerField(null=True,blank=True,verbose_name="আয়")
    file=models.FileField(upload_to='media/member_file/%Y',blank=True,null=True,verbose_name="মেম্বারের সুপারিশ ফাইল")
    nid_file=models.FileField(upload_to='media/nid_file/%Y',blank=True,null=True,verbose_name="এনআইডি-জন্ম নিবন্ধন")
    transaction=models.ForeignKey(Transaction,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="ট্রান্সেকশন")
    tracking_no=models.CharField(max_length=25,null=True, blank=True,verbose_name="ট্র্যাকিং নং")
    is_verified=models.BooleanField(default=False,verbose_name="ভেরিফাইড কিনা?")
    chairman=models.ForeignKey(Chairman,on_delete=models.SET_NULL,blank=True,null=True,verbose_name="চেয়ারম্যান")
    secretary=models.ForeignKey(Secretary,on_delete=models.SET_NULL,blank=True,null=True,verbose_name="সচিব")
    member=models.ForeignKey(Member,on_delete=models.SET_NULL,blank=True,null=True,verbose_name="সদস্য")
    language=models.CharField(max_length=250,blank=True,null=True,verbose_name="ভাষা")
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    
    class Meta:
        verbose_name="লাইসেন্সসমূহ"
        verbose_name_plural="লাইসেন্সসমূহ"

    def __str__(self):
        return self.licensed_name +':'+ str(self.phone)
   
    
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
