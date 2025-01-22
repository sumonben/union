from django.contrib import admin
from django.urls import path,include, re_path
from . import views

urlpatterns = [
    
        path('proceed_payment/', views.ProceedPayment, name='proceed_payment'),
        path('success/', views.CheckoutSuccessView.as_view(), name='success'),
        path('failed/', views.CheckoutFaildView.as_view(), name='failed'),
        path('canceled/', views.CheckoutCanceledView.as_view(), name='canceled'),





]