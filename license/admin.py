from django.contrib import admin
from certificate.models import Certificate,Adress,Person,CertificateType,Relation,Cause
from .models import License,LicenseType
from import_export.admin import ExportActionMixin,ImportExportMixin
# Register your models here.

@admin.register(License)
class LicenseAdmin(ImportExportMixin,admin.ModelAdmin):
    search_fields=[  'email','phone',]
    list_display=[ 'tracking_no','memorial_no','license_owner_name','licensed_name','email','phone','transaction_detaills','paid_at','is_verified','created_at',]
    list_display_links = ['tracking_no','memorial_no','license_owner_name','email','phone',]
    list_filter=['is_verified','created_at',]
    filter_horizontal = ['person',]

    
    def change_view(self, request, object_id, extra_context=None):
        license=License.objects.filter(id=object_id).first()
        print(license.person)
        self.exclude=('description',)
        
        return super(LicenseAdmin, self).change_view(request, object_id, extra_context=None)


# @admin.register(WarishanLicense)
# class WarishanLicenseAdmin(ImportExportMixin,admin.ModelAdmin):
#     search_fields=[  'email','phone',]
#     list_display=[ 'name','tracking_no','email','phone','transaction_detaills','paid_at','is_verified']
#     list_display_links = ['name','email','phone',]
#     list_filter=['is_verified']


@admin.register(LicenseType)
class LicenseTypeAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=['id','serial','name','template']
