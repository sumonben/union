from django.contrib import admin
from .models import Member,Chairman,Post,Secretary
from import_export.admin import ImportExportMixin
from admin_auto_filters.filters import AutocompleteFilter


class UnionFilter(AutocompleteFilter):
    title = 'Union' # display title
    field_name = 'union' # name of the foreign key field
# Register your models here.
@admin.register(Chairman)
class ChairAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','union']
    list_display_links = ['name','name_en']
    search_fields = ['name','name_en','union']
    list_filters = [UnionFilter]

@admin.register(Secretary)
class SecretaryAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','union']
    list_display_links = ['name','name_en']
    search_fields = ['name','name_en','union']


@admin.register(Member)
class MemberAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','ward']
    list_display_links = ['name','name_en']
    search_fields = ['name','name_en']
    # autocomplete_fields = ['ward',]

@admin.register(Post)
class PostAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en']
    list_display_links = ['name','name_en']
    search_fields = ['name','name_en']
    
# admin.site.register(Member, MemberAdmin)