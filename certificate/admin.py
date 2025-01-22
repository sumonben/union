from django.contrib import admin
from .models import Certificate,Adress,WarishanCertificate,Warish,CertificateType
from import_export.admin import ExportActionMixin,ImportExportMixin
# Register your models here.

@admin.register(Certificate)
class CertificateAdmin(ImportExportMixin,admin.ModelAdmin):
    search_fields=[  'email','phone',]
    list_display=[ 'name','email','phone','transaction_detaills','paid_at','is_verified']
    list_display_links = ['name','email','phone',]
    list_filter=['is_verified']

@admin.register(WarishanCertificate)
class WarishanCertificateAdmin(ImportExportMixin,admin.ModelAdmin):
    search_fields=[  'email','phone',]
    list_display=[ 'name','email','phone','transaction_detaills','paid_at','is_verified']
    list_display_links = ['name','email','phone',]
    list_filter=['is_verified']

@admin.register(Warish)
class WarishAdmin(ExportActionMixin,admin.ModelAdmin):
    pass

@admin.register(Adress)
class AdressAdmin(ExportActionMixin,admin.ModelAdmin):
    pass
@admin.register(CertificateType)
class CertificateTypeAdmin(ExportActionMixin,admin.ModelAdmin):
    pass
