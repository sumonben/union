from django.db import models
from region.models import Division, District, Upazilla, Union, PostOffice

class UnionType(models.Model):
    serial=models.IntegerField(default=0)
    name=models.CharField(max_length=50)
    name_en=models.CharField(max_length=50)
    class Meta:
        ordering = ['serial']
        verbose_name="ইউনিয়ন বা পৌরসভার ধরণ "
        verbose_name_plural="ইউনিয়ন বা পৌরসভার ধরণ"
    def __str__(self):
        return self.name+'('+self.name_en+')'

class UnionDetails(models.Model):
    name=models.CharField(max_length=50)
    name_en=models.CharField(max_length=50)
    name_short=models.CharField(max_length=50,blank=True,null=True)
    name_short_en=models.CharField(max_length=50,blank=True,null=True)
    post_office=models.ForeignKey(PostOffice, on_delete=models.SET_NULL,blank=True,null=True)
    upazilla=models.ForeignKey(Upazilla, on_delete=models.SET_NULL,blank=True,null=True)
    district=models.ForeignKey(District, on_delete=models.SET_NULL,blank=True,null=True)
    union_type=models.ForeignKey(UnionType, on_delete=models.SET_NULL,blank=True,null=True)
    union_code=models.CharField(max_length=50,blank=True,null=True)
    logo=models.FileField(upload_to='media/logo',blank=True,null=True,)
    logo_en=models.FileField(upload_to='media/logo',blank=True,null=True,)
    logo_opacity=models.FileField(upload_to='media/logo',blank=True,null=True,)
    logo_opacity_en=models.FileField(upload_to='media/logo',blank=True,null=True,)
    monogram=models.FileField(upload_to='media/logo',blank=True,null=True)
    monogram_en=models.FileField(upload_to='media/logo',blank=True,null=True)
    link=models.URLField(max_length=200, blank=True, null=True)
    is_active=models.BooleanField(default=False)

    class Meta:
        ordering = ['name_en']
        verbose_name="ইউনিয়ন বা পৌরসভা বিবরণ"
        verbose_name_plural="ইউনিয়ন বা পৌরসভা বিবরণ"

    def __str__(self):
        return self.name+'('+self.name_en+')'

class ImportantLinks(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=500, blank=True, null=True)
    title_en=models.CharField(max_length=500, blank=True, null=True)
    link=models.URLField(max_length=200, blank=True, null=True)
    class Meta:
        ordering = ['serial']
        verbose_name="লিংকসমূহ"
        verbose_name_plural="লিংকসমূহ"
    def __str__(self):
        if self.title:
            return self.title
        else:
            return '1'

class ColorRoot(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=100,unique=True)
    title_en=models.CharField(max_length=100,unique=True)
    body=models.CharField(max_length=50,blank=True,null=True)
    weather=models.CharField(max_length=50,blank=True,null=True)
    service=models.CharField(max_length=50,blank=True,null=True)
    card=models.CharField(max_length=50,blank=True,null=True)
    heading=models.CharField(max_length=50,blank=True,null=True)
    sub_heading=models.CharField(max_length=50,blank=True,null=True)
    navitem=models.CharField(max_length=50,blank=True,null=True)
    navbar_collaps=models.CharField(max_length=50,blank=True,null=True)
    member_registration=models.CharField(max_length=50,blank=True,null=True)
    internal=models.CharField(max_length=50,blank=True,null=True)
    other_text=models.CharField(max_length=50,blank=True,null=True)
    union_details=models.ForeignKey(UnionDetails, on_delete=models.SET_NULL,blank=True,null=True)
    is_active=models.BooleanField(default=False)
    class Meta:
        ordering = ['serial']
        verbose_name="কালারসমূহ"
        verbose_name_plural="কালারসমূহ"
    def __str__(self):
        return self.title+'('+self.title_en+')'

 