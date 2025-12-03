from django.contrib import admin
from .models import UnionDetails,ImportantLinks, UnionType, ColorRoot, DeveloperDetails
from import_export.admin import ExportActionMixin,ImportExportMixin
from admin_auto_filters.filters import AutocompleteFilter

@admin.register(UnionType)
class UnionTypeAdmin(ImportExportMixin,admin.ModelAdmin):
    pass
@admin.register(UnionDetails)
class UnionDetailsAdmin(ImportExportMixin,admin.ModelAdmin):
    pass
@admin.register(ImportantLinks)
class ImportantLinksAdmin(ImportExportMixin,admin.ModelAdmin):
    pass
@admin.register(DeveloperDetails)
class DeveloperDetailsAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[   'serial','title','title_en']

@admin.register(ColorRoot)
class ColorRootAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display=[   'serial','title','title_en','body',
    'weather',
    'service',
    'card',
    'heading',
    'sub_heading',
    'navitem',
    'navbar_collaps',
    'member_registration',
    'internal',
    'other_text',
    'union_details',
    'is_active']
    search_fields=[  'title','title_en']
    list_display_links = ['serial','title']
    list_editable=[ 'title_en','body',
    'weather',
    'service',
    'card',
    'heading',
    'sub_heading',
    'navitem',
    'navbar_collaps',
    'member_registration',
    'internal',
    'other_text',
    'is_active']