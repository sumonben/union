from django.contrib import admin
from .models import Transaction,PaymentPurpose,PaymentType,PaymentGateway,PaymentURL
from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)
# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('name','tracking_no','email','phone', 'card_no', 'amount', 'tran_id','tran_purpose','status', 'created_at',)
    search_fields = ('tracking_no','phone', 'status')
    list_filter=( 'created_at',("created_at", DateRangeFilterBuilder()),)


admin.site.register(PaymentGateway)
admin.site.register(PaymentURL)

@admin.register(PaymentPurpose)
class UserAdmin(admin.ModelAdmin):
    list_display=[  'id','serial','certificate_type_id','title','title_en','payment_type']
    filter_fields=[  'id','title','title_en']

@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display=[  'id','serial','title','title_en']
    filter_fields=[  'id','title','title_en']
