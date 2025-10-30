from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import HoldingType, HoldingTax, FiscalYear
from account.models import Chairman
from region.models import UnionDetails
from .forms import  HoldingTaxForm, HoldingTaxSearchForm
from certificate.forms import  AdressForm
from django.views.generic import View
from django.contrib import messages
from payment.sslcommerz import sslcommerz_payment_gateway_holdingtax
from payment.models import Transaction,PaymentPurpose,PaymentType

# Create your views here.
class HoldingTaxSearch(View):
    model = HoldingTax()
    template_name = 'holdingtax/holdingtax_search.html'
    def get(self, request, *args, **kwargs):
        context={}
        form=HoldingTaxSearchForm()
        context['form']=form
        return render(request,self.template_name,context)
    def post(self, request, *args, **kwargs):
        context={}
        fiscal_year=FiscalYear.objects.filter(id=request.POST.get('fiscal_year')).first()
        holding_tax=HoldingTax.objects.filter(holding_no=request.POST.get('holding_no').strip(),fiscal_year=request.POST.get('fiscal_year')).first()

        if holding_tax:
            if holding_tax.transaction and holding_tax.is_paid == True:
                messages.error(request, 'আপনার '+fiscal_year.title+' অর্থবছরের হোল্ডিং ট্যাক্সটি প্রদান করা হয়েছে')
                return redirect('holding_tax')
            form=HoldingTaxForm(instance=holding_tax)
            adress_form=AdressForm()
            context['adress_form']=adress_form
            context['form']=form
            return render(request,'holdingtax/holdingtax.html',context)
       
        messages.error(request, 'আপনার তথ্য সঠিক নয়! সঠিক তথ্য দিয়ে আবার চেষ্টা করুন')
        return redirect('holding_tax')

        
class PayHoldingTax(View):
    model = HoldingTax()
    template_name = 'holdingtax/holdingtax.html'
    def get(self, request, *args, **kwargs):
        context={}
        form=HoldingTaxForm(instance=2)
        adress_form=AdressForm()
        context['adress_form']=adress_form
        context['form']=form
        return render(request,self.template_name,context)
    def post(self, request, *args, **kwargs):
        context={}
        holding_tax=HoldingTax.objects.filter(holding_no=request.POST.get('holding_no').strip(),fiscal_year=request.POST.get('fiscal_year')).first()
        payment_purpose=PaymentPurpose.objects.filter(certificate_type_id=holding_tax.holding_type.id,payment_type_id=3).first()
        if payment_purpose:
            return redirect(sslcommerz_payment_gateway_holdingtax(request, holding_tax, holding_tax.holding_type, payment_purpose))
        
        payment_purpose=PaymentPurpose.objects.create(
                serial=0,
                certificate_type_id=holding_tax.holding_type.id,
                title =holding_tax.holding_type.name,
                payment_type_id=3,
                

            )
        return redirect(sslcommerz_payment_gateway_holdingtax(request, holding_tax, holding_tax.holding_type, payment_purpose))

class HoldingTaxDownload(View):
    model = HoldingTax()
    template_name = 'holdingtax/holdingtax_search.html'
    def get(self, request, *args, **kwargs):
        context={}
        form=HoldingTaxSearchForm()
        context['form']=form
        context['type']='download'
        return render(request,self.template_name,context)
    def post(self, request, *args, **kwargs):
        context={}
        holding_tax=HoldingTax.objects.filter(holding_no=request.POST.get('holding_no').strip(),fiscal_year=request.POST.get('fiscal_year')).first()
        union_details=UnionDetails.objects.last()
        transaction=Transaction.objects.filter(tracking_no=request.POST.get('holding_no').strip()).first()
        chairman=Chairman.objects.filter(is_active=True).last()
        context['holding_tax']=holding_tax
        context['holding_type']=holding_tax.holding_type
        context['union_details']=union_details
        context['transaction']=transaction
        context['chairman']=chairman
        context['tran_purpose']=transaction.tran_purpose
        return render(request,'payment/payment_receipt_holdingtax.html',context)

