from django.contrib import admin
from .models import Division,District,Union,Upazilla,Ward,Village,PostOffice,Mouja,OthersAdress
from import_export.admin import ExportActionMixin,ImportExportMixin
from admin_auto_filters.filters import AutocompleteFilter

# Register your models here.
@admin.register(Division)
class DivisionAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','link']
    list_display_links = ['name','name_en']
@admin.register(District)
class DistrictAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','division','link']
    list_display_links = ['name','name_en']
    list_filter=['division']
    search_fields = ['name','name_en','division']

@admin.register(Upazilla)
class UpazillaAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','district','link']
    list_display_links = ['name','name_en']
    list_filter=['district']
    search_fields = ['name','name_en','district']
    #autocomplete_fields = ['district',]

@admin.register(Union)
class UnionAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','upazilla','link']
    list_display_links = ['name','name_en']
    search_fields = ['name','name_en','upazilla']
    #autocomplete_fields = ['upazilla',]

@admin.register(Ward)
class WordAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','link']
    list_display_links = ['name','name_en']
    search_fields = ['name','name_en']
    # autocomplete_fields = ['union',]

@admin.register(PostOffice)
class PostOfficeAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','post_code','link']
    list_display_links = ['name','name_en']
    search_fields = ['name','name_en']

@admin.register(Village)
class VillageAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','ward','link']
    list_display_links = ['name','name_en']
    search_fields = ['name','name_en','ward']
    # autocomplete_fields = ['ward',]
@admin.register(Mouja)
class MoujaAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','village','ward','link']
    list_display_links = ['name','name_en']
    search_fields = ['name','name_en','ward']
    # autocomplete_fields = ['ward','village',]
@admin.register(OthersAdress)
class AdressAdmin(ExportActionMixin,admin.ModelAdmin):
    pass