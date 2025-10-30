from django.contrib import admin
from django.urls import path,include, re_path
import static
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django import views as django_views


urlpatterns = [
    path('',views.HoldingTaxSearch.as_view(), name='holding_tax'),
    path('pay_holdingtax/',views.PayHoldingTax.as_view(), name='pay_holdingtax'),
    path('download_holdingtax/',views.HoldingTaxDownload.as_view(), name='download_holdingtax'),
]