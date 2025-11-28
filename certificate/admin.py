from django.contrib import admin
from .models import Certificate,Adress,Person,CertificateType,Relation,Cause,Gender,MaritalStatus
from import_export.admin import ExportActionMixin,ImportExportMixin
# Register your models here.

@admin.register(Certificate)
class CertificateAdmin(ImportExportMixin,admin.ModelAdmin):
    search_fields=[ 'phone','tracking_no']
    list_display=[ 'tracking_no','memorial_no','name','phone','certificate_type','transaction_detaills','paid_at','is_verified','created_at',]
    list_display_links = ['tracking_no','memorial_no','name','phone',]
    list_filter=['is_verified','created_at','certificate_type',]
    filter_horizontal = ['person','others_adress']

    
    def change_view(self, request, object_id, extra_context=None):
        certificate=Certificate.objects.filter(id=object_id).first()
        self.exclude=('others_adress',)
        if certificate.certificate_type.id != 1 and certificate.certificate_type.id != 9 and certificate.certificate_type.id != 7 and certificate.certificate_type.id != 10 and certificate.certificate_type.id != 15 and certificate.certificate_type.id != 25 and certificate.certificate_type.id != 28:   
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
class WarishAdmin(ImportExportMixin,admin.ModelAdmin):
    search_fields=[  'tracking_no','name']
    list_display=[ 'tracking_no','name','relation']
    list_display_links = ['tracking_no','name']
@admin.register(Cause)
class CauseAdmin(ImportExportMixin,admin.ModelAdmin):
    pass
@admin.register(Relation)
class RelationAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'id','name','name_en']
@admin.register(Gender)
class GenderAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'id','name','name_en']
    pass
@admin.register(MaritalStatus)
class MaritalStatusAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'id','name','name_en']

@admin.register(Adress)
class AdressAdmin(ImportExportMixin,admin.ModelAdmin):
    pass
@admin.register(CertificateType)
class CertificateTypeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=['id','serial','name','template','main_body_bg','header_bg','title_bg','body_bg','heading_color','subheading_color','title_color']
    list_display_links=['id','serial','name','template']
    list_editable=['main_body_bg','header_bg','title_bg','body_bg','heading_color','subheading_color','title_color']

