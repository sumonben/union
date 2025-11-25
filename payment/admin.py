from django.contrib import admin
from .models import Transaction,PaymentPurpose,PaymentType,PaymentGateway,PaymentURL
from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)
from import_export.admin import ExportActionMixin,ImportExportMixin

# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name','tracking_no','email','phone', 'card_no', 'amount', 'tran_id','tran_purpose','status', 'created_at',)
    search_fields = ('tracking_no','phone', 'status')
    list_filter=( 'created_at',("created_at", DateRangeFilterBuilder()),)

@admin.register(PaymentGateway)
class PaymentGatewayAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display=[ 'gateway_name','store_id', 'store_pass', 'is_sandbox', 'is_active']
    filter_fields=['is_active',]


@admin.register(PaymentPurpose)
class UserAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[  'id','serial','certificate_type_id','title','title_en','payment_type']
    filter_fields=[  'id','title','title_en']

@admin.register(PaymentType)
class PaymentTypeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display=[  'id','serial','title','title_en']
    filter_fields=[  'id','title','title_en']
