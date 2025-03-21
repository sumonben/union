from django.contrib import admin
from .models import Certificate,Adress,Person,CertificateType,Relation,Cause,Gender
from import_export.admin import ExportActionMixin,ImportExportMixin
# Register your models here.

@admin.register(Certificate)
class CertificateAdmin(ImportExportMixin,admin.ModelAdmin):
    search_fields=[  'email','phone',]
    list_display=[ 'tracking_no','memorial_no','name','email','phone','certificate_type','transaction_detaills','paid_at','is_verified']
    list_display_links = ['tracking_no','memorial_no','name','email','phone',]
    list_filter=['is_verified']

# @admin.register(WarishanCertificate)
# class WarishanCertificateAdmin(ImportExportMixin,admin.ModelAdmin):
#     search_fields=[  'email','phone',]
#     list_display=[ 'name','tracking_no','email','phone','transaction_detaills','paid_at','is_verified']
#     list_display_links = ['name','email','phone',]
#     list_filter=['is_verified']

@admin.register(Person)
class WarishAdmin(ExportActionMixin,admin.ModelAdmin):
    pass
@admin.register(Cause)
class CauseAdmin(ExportActionMixin,admin.ModelAdmin):
    pass
@admin.register(Relation)
class RelationAdmin(ExportActionMixin,admin.ModelAdmin):
    pass
@admin.register(Gender)
class GenderAdmin(ExportActionMixin,admin.ModelAdmin):
    pass

@admin.register(Adress)
class AdressAdmin(ExportActionMixin,admin.ModelAdmin):
    pass
@admin.register(CertificateType)
class CertificateTypeAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=['id','name','template']
