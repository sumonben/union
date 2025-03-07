from django.shortcuts import render
from .models import License,LicenseType
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import LicenseType,License
from certificate.models import CertificateType,Certificate,Person,Adress
from payment.models import Transaction
from account.models import Chairman, Member,Secretary
from .forms import LicenseTypeForm,LicenseForm,AdressFormSet,LicenceDownloadForm
from certificate.forms import AdressForm,WarishFormSet,WarishForm,SamePersonFormSet,AdressFormExtra
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from certificate.views import gernerate_tracking_no
from django.forms import formset_factory
from payment.sslcommerz import sslcommerz_payment_gateway

import string
import random



class ApplyForLicense(View):
    model = LicenseType()
    template_name = 'forms/license_form.html'
    def get(self, request, id, *args, **kwargs):
        context={}
        certificate_type=CertificateType.objects.filter(id=id).first()
        context['certificate_type']=certificate_type
        certificate_types=CertificateType.objects.all().order_by('serial')
        context['certificate_types']=certificate_types
        
        license_type=LicenseType.objects.filter(id=id).first()
        context['license_type']=license_type
        license_types=LicenseType.objects.all().order_by('serial')
        context['license_types']=license_types
        form=LicenseForm(instance=license_type)
        form.license_type=license_type
        adress_form=AdressForm()
        if license_type.id == 1:
            formset = SamePersonFormSet(queryset=Person.objects.none()) 
            formset_adress = AdressFormSet(queryset=Adress.objects.none())
            context['formset']=formset
            context['formset_adress']=formset_adress
            adress_form_extra=AdressFormExtra()
            context['adress_form_extra']=adress_form_extra

        context['form']=form
        context['adress_form']=adress_form
              
        return render(request,self.template_name,context)
    
    def post(self, request,id, *args, **kwargs):
        context={}
        license_types=LicenseType.objects.all().order_by('serial')
        context['license_types']=license_types
        license_type=LicenseType.objects.filter(id=id).first()
        context['license_type']=license_type
        return render(request,self.template_name,context)

class LicenseView(View):
    model = License
    template_name = 'forms/license_form.html'
    def get(self, request, *args, **kwargs):
        context={}
        license_types=LicenseType.objects.all().order_by('serial')
        context['license_types']=license_types
        form=LicenseForm()
        adress_form=AdressForm()
        formset = WarishFormSet(queryset=Person.objects.none())
        context['form']=form
        context['adress_form']=adress_form
        context['formset']=formset
        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        context={}
        adress_form_extra=None
        formset=None
        form = LicenseForm(request.POST, request.FILES)
        adress_form = AdressForm(data=self.request.POST)

        
        formset = SamePersonFormSet(data=self.request.POST)
        formset1 = AdressFormSet(data=self.request.POST)

       
           

        license_types=LicenseType.objects.all().order_by('serial')
        context['license_types']=license_types
        license=License.objects.filter(phone=request.POST.get('phone')).first()
        if license:
            if license.transaction == None:
                license.delete()
        tracking_no=gernerate_tracking_no()
        # Check if submitted forms are valid
        if form.is_valid():
            license=form.save(commit=False)
            person=None
            adress=None
            adress_of_license=None
            if adress_form.is_valid:
                license.adress=adress_form.save()
            if formset1.is_valid():
                #print(formset1)
                adresses=formset1.save()
               
                for fs in adresses:
                    license.adress_of_license=fs
                   

                    
            license.tracking_no=tracking_no
            chairman=Chairman.objects.all().order_by('-id').first()
            secretary=Secretary.objects.all().order_by('-id').first()
            member=Member.objects.filter(ward=license.adress.village.ward).last()
            license.chairman=chairman
            license.secretary=secretary
            license.member=member
            license.language=request.POST.get('language')
            license.income=request.POST.get('income')
            license.profession=request.POST.get('profession')
            license.caste=request.POST.get('caste')
            license.description=request.POST.get('description')
            
            license.save()

            license=License.objects.filter(tracking_no=tracking_no).first()

            context['license']=license
            return render(request,'license/applicant_details.html',context)

        
        return HttpResponse('nothing to see')


class submitLicenseFormView(View):
    model = License
    template_name = 'license/applicant_details.html'
    def post(self, request, *args, **kwargs):
        license=License.objects.filter(tracking_no=request.POST.get('tracking_no')).first()
        license_type=license.license_type
        type=2
        return redirect(sslcommerz_payment_gateway(request, license, license_type, type))
    
class DownloadLicenseView(View):
    model = License
    template_name = 'license/download_license_form.html'
    def get(self, request, *args, **kwargs):
        context={}
        license_types=LicenseType.objects.all().order_by('serial')
        context['license_types']=license_types
        form=LicenceDownloadForm()
        context['form']=form
        return render(request,self.template_name, context)
    def post(self, request, *args, **kwargs):
        context={}
        license_type=LicenseType.objects.all().order_by('serial')
        context['license_type']=license_type
        license=License.objects.filter(tracking_no=request.POST.get('tracking_no'),license_type=request.POST.get('license_type')).first()
        transaction=Transaction.objects.filter(tracking_no=request.POST.get('tracking_no')).first()
        if license:
            if transaction:
                if license.is_verified==False:
                    context['message']="আপনার আবেদনটি এখনো অনুমোদিত হয়নি, অপেক্ষা করুন"
                    form=LicenceDownloadForm()
                    context['form']=form
                    return render(request,self.template_name, context)
                

                license_type=license.license_type
                context['license']=license
                context['license_type']=license_type

                if license_type.id == 1:
                    return render(request,'license/trade_license.html', context)
               
                
                return render(request,'license/trade_license.html', context)
            context['message']="দুখিঃত! আপনার সনদটির জন্য পেমেন্ট করা হয়নি"
            form=LicenceDownloadForm()
            context['form']=form
            return render(request,self.template_name, context)
        context['message']="দুখিঃত! সঠিক সনদ বাছাই করুন বা সঠিক ট্র্যাকিং নং প্রবেশ করান"
        form=LicenceDownloadForm()
        context['form']=form
        return render(request,self.template_name, context)
