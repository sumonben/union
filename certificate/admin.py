from django.contrib import admin
from .models import Certificate,Division,District,Union,Upazilla,Adress,WarishanCertificate
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
@admin.register(Division)
class DivisionAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','link']
    list_display_links = ['name','name_en']
@admin.register(District)
class DistrictAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','division','link']
    list_display_links = ['name','name_en']
    list_filter=['division']

@admin.register(Upazilla)
class UpazillaAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','district','link']
    list_display_links = ['name','name_en']
    list_filter=['district']

@admin.register(Union)
class UnionAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','upazilla','link']
    list_display_links = ['name','name_en']
@admin.register(Adress)
class AdressAdmin(ExportActionMixin,admin.ModelAdmin):
    pass