from django.contrib import admin
from .models import Member,Chairman,Post
from import_export.admin import ImportExportMixin
# Register your models here.
@admin.register(Chairman)
class ChairAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','union']
    list_display_links = ['name','name_en']
    search_fields = ['name','name_en','union']
    autocomplete_fields = ['union',]

@admin.register(Member)
class MemberAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','ward']
    list_display_links = ['name','name_en']
    search_fields = ['name','name_en']
    autocomplete_fields = ['ward',]

@admin.register(Post)
class PostAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en']
    list_display_links = ['name','name_en']
    search_fields = ['name','name_en']
    
