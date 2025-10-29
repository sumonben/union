from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import HoldingType, HoldingTax
from .forms import  HoldingTaxForm, HoldingTaxSearchForm
from certificate.forms import  AdressForm
from django.views.generic import View
from django.contrib import messages
from payment.sslcommerz import sslcommerz_payment_gateway_holdingtax

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
        holding_tax=HoldingTax.objects.filter(holding_no=request.POST.get('holding_no').strip(),fiscal_year=request.POST.get('fiscal_year')).first()
        # return HttpResponse(holding_no)
        if holding_tax:
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
        return redirect(sslcommerz_payment_gateway_holdingtax(request, holding_tax, holding_tax.holding_type,'holdingtax'))
