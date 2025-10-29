from django.contrib import admin
from .models import HoldingType, HoldingTax,FiscalYear
from import_export.admin import ExportActionMixin,ImportExportMixin
# Register your models here.

@admin.register(FiscalYear)
class FiscalYearTypeAdmin(ImportExportMixin,admin.ModelAdmin):
    search_fields=[ 'title']
    list_display=[ 'serial','title','title_en',]
    list_display_links = ['serial','title',]
@admin.register(HoldingType)
class HoldingTypeAdmin(ImportExportMixin,admin.ModelAdmin):
    search_fields=[ 'name']
    list_display=[ 'serial','name','name_en',]
    list_display_links = ['serial','name',]
    list_filter=['is_active',]
@admin.register(HoldingTax)
class HoldingTaxAdmin(ImportExportMixin,admin.ModelAdmin):
    search_fields=[ 'holding_no']
    list_display=[ 'holding_no','name','phone','holding_type','village','ward','post_office','transaction','is_paid','fiscal_year']
    list_display_links = ['holding_no','name','phone',]
    list_filter=['is_paid','fiscal_year','holding_type','ward']
