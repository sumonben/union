from django.contrib import admin
from certificate.models import Certificate,Adress,Person,CertificateType,Relation,Cause
from .models import License,LicenseType
from import_export.admin import ExportActionMixin,ImportExportMixin
# Register your models here.

@admin.register(License)
class LicenseAdmin(ImportExportMixin,admin.ModelAdmin):
    search_fields=[  'email','phone',]
    list_display=[ 'tracking_no','license_owner_name','licensed_name','email','phone','transaction_detaills','paid_at','is_verified']
    list_display_links = ['license_owner_name','email','phone',]
    list_filter=['is_verified']

# @admin.register(WarishanLicense)
# class WarishanLicenseAdmin(ImportExportMixin,admin.ModelAdmin):
#     search_fields=[  'email','phone',]
#     list_display=[ 'name','tracking_no','email','phone','transaction_detaills','paid_at','is_verified']
#     list_display_links = ['name','email','phone',]
#     list_filter=['is_verified']


@admin.register(LicenseType)
class LicenseTypeAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=['id','serial','name']
