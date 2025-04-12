from django.contrib import admin
from .models import Certificate,Adress,Person,CertificateType,Relation,Cause,Gender
from import_export.admin import ExportActionMixin,ImportExportMixin
# Register your models here.

@admin.register(Certificate)
class CertificateAdmin(ImportExportMixin,admin.ModelAdmin):
    search_fields=[  'email','phone','tracking_no']
    list_display=[ 'tracking_no','memorial_no','name','email','phone','certificate_type','transaction_detaills','paid_at','is_verified','created_at']
    list_display_links = ['tracking_no','memorial_no','name','email','phone',]
    list_filter=['is_verified','created_at','certificate_type',]
    filter_horizontal = ['person','others_adress']

    
    def change_view(self, request, object_id, extra_context=None):
        certificate=Certificate.objects.filter(id=object_id).first()
        self.exclude=('others_adress',)
        if certificate.certificate_type.id != 1 and certificate.certificate_type.id != 9 and certificate.certificate_type.id != 7 and certificate.certificate_type.id != 10 and certificate.certificate_type.id != 15 :   
            self.exclude = self.exclude=self.exclude+ ('person', )
        if certificate.certificate_type.id != 8 and certificate.certificate_type.id != 21 and certificate.certificate_type.id != 4 and certificate.certificate_type.id != 12 and certificate.certificate_type.id != 16 :   
            self.exclude = self.exclude=self.exclude+ ('description', )
        if certificate.certificate_type.id != 8 and certificate.certificate_type.id == 2 :   
            self.exclude = self.exclude=self.exclude+ ('description','profession','income','caste','date','dob','amount','cause' )
        return super(CertificateAdmin, self).change_view(request, object_id, extra_context=None)

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
    list_display=['id','serial','name','template']
    list_display_links=['id','serial','name','template']
