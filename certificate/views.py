from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Person,CertificateType,Certificate,Cause
from license.models import LicenseType,License
from payment.models import Transaction,PaymentPurpose,PaymentType
from account.models import Chairman, Member,Post,Secretary
from .forms import AdressForm,WarishFormSet,WarishForm,SamePersonFormSet,CertificateTypeForm,CertificateForm,CertificateDownloadForm,OtherAdressFormSet
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.forms import formset_factory
from region.forms import OthersAdressForm
from payment.sslcommerz import sslcommerz_payment_gateway
from django.contrib import messages
from django.views.decorators.cache import cache_page
from django.core.cache import cache


import string
import random
# Create your views here.

def gernerate_tracking_no( size=8, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


class FrontView(View):
    model = Certificate()
    template_name = 'front.html'
    def get(self, request, *args, **kwargs):
        certificate_types=CertificateType.objects.all().order_by('serial')
        license_types=LicenseType.objects.all().order_by('serial')
        context={}
        context['certificate_types']=certificate_types
        context['license_types']=license_types
        return render(request,'front.html',context)
    def post(self, request, *args, **kwargs):
        context={}
        return render(request,'front.html',context)

class ContactView(View):
    model = Certificate()
    template_name = 'contact.html'
    def get(self, request, *args, **kwargs):
        context={}
        # certificate_types_first=CertificateType.objects.all().order_by('serial')[:4]
        certificate_types=CertificateType.objects.all().order_by('serial')
        license_types=LicenseType.objects.all().order_by('serial')
        chairman=Chairman.objects.all().order_by('-id').first()
        secretary=Secretary.objects.all().order_by('-id').first()
        member=Member.objects.all().order_by('-id').first() 
        context={}
        context['certificate_types']=certificate_types
        # context['certificate_types_first']=certificate_types_first
        context['license_types']=license_types
        context['chairman']=chairman
        context['secretary']=secretary
        context['member']=member
        context['member']=member
        cache.clear()
        return render(request,'contact.html',context)
    def post(self, request, *args, **kwargs):
        context={}
        return render(request,'home.html',context)


class HomeView(View):
    model = Certificate()
    template_name = 'home.html'
    def get(self, request, *args, **kwargs):
        context={}
        # certificate_types_first=CertificateType.objects.all().order_by('serial')[:4]
        certificate_types=CertificateType.objects.all().order_by('serial')
        license_types=LicenseType.objects.all().order_by('serial')
        chairman=Chairman.objects.all().order_by('-id').first()
        secretary=Secretary.objects.all().order_by('-id').first()
        certificate_count1=Certificate.objects.filter(is_verified=True).count()
        certificate_count2=Certificate.objects.filter(is_verified=False).count()
        license_count1=License.objects.filter(is_verified=True).count()
        license_count2=License.objects.filter(is_verified=True).count()

        count=certificate_count1+license_count1

            
        context={}
        context['certificate_types']=certificate_types
        # context['certificate_types_first']=certificate_types_first
        context['license_types']=license_types
        context['chairman']=chairman
        context['secretary']=secretary
        context['certificate_count1']=  certificate_count1      
        context['certificate_count2']= certificate_count2       
        context['license_count1']= license_count1       
        context['license_count2']=license_count2
        context['count']=count
        cache.clear()
        return render(request,'home.html',context)
    def post(self, request, *args, **kwargs):
        context={}
        return render(request,'home.html',context)

class ApplyForCertificate(View):
    model = CertificateType()
    template_name = 'forms/certificate_form.html'
    def get(self, request, id, *args, **kwargs):
        context={}
        certificate_type=CertificateType.objects.filter(id=id).first()
        context['certificate_type']=certificate_type
        certificate_types=CertificateType.objects.all().order_by('serial')
        context['certificate_types']=certificate_types
        license_types=LicenseType.objects.all().order_by('serial')
        context['license_types']=license_types
        form=CertificateForm(instance=certificate_type)
        form.certificate_type=certificate_type
        adress_form=AdressForm()
        context['form']=form
        context['adress_form']=adress_form
        if certificate_type.id== 1 or certificate_type.id== 7 :
            formset = WarishFormSet(queryset=Person.objects.none())
            context['formset']=formset
        if certificate_type.id== 9 or certificate_type.id == 15 or certificate_type.id == 25 or certificate_type.id == 10 :
            formset = SamePersonFormSet(queryset=Person.objects.none())
            context['formset']=formset
        

        
        return render(request,self.template_name,context)
    
    def post(self, request,id, *args, **kwargs):
        print('post: ',id)
        context={}
        certificate_types=CertificateType.objects.all().order_by('serial')
        context['certificate_types']=certificate_types
        license_types=LicenseType.objects.all().order_by('serial')
        context['license_types']=license_types
        return render(request,self.template_name,context)

    
class SelectCertificate(View):
    model = CertificateType()
    template_name = 'forms/certificate_form.html'
    def get(self, request, *args, **kwargs):
        context={}
        certificate_types=CertificateType.objects.all().order_by('serial')
        context['certificate_types']=certificate_types
        license_types=LicenseType.objects.all().order_by('serial')
        context['license_types']=license_types
        form=CertificateTypeForm()
        context['form']=form
        return render(request,'certificate/select_certificate.html',context)
    def post(self, request, *args, **kwargs):
        context={}
        print(request.POST.get('name'))
        certificate_type=CertificateType.objects.filter(id=request.POST.get('name')).first()
        context['certificate_type']=certificate_type
        certificate_types=CertificateType.objects.all().order_by('serial')
        context['certificate_types']=certificate_types
        license_types=LicenseType.objects.all().order_by('serial')
        context['license_types']=license_types
        form=CertificateForm(instance=certificate_type)
        form.certificate_type=certificate_type
        adress_form=AdressForm()
        context['form']=form
        context['adress_form']=adress_form
           
        if certificate_type.id== 1:
            formset = WarishFormSet(queryset=Person.objects.none())
            context['formset']=formset
        if certificate_type.id== 9 or certificate_type.id == 15 or certificate_type.id == 25 :
            formset = SamePersonFormSet(queryset=Person.objects.none())
            context['formset']=formset
                
         
        return render(request,self.template_name,context)
        

class CertificateView(View):
    model = Certificate
    template_name = 'forms/certificate_form.html'
    def get(self, request, *args, **kwargs):
        context={}
        certificate_types=CertificateType.objects.all().order_by('serial')
        context['certificate_types']=certificate_types
        license_types=LicenseType.objects.all().order_by('serial')
        context['license_types']=license_types
        form=CertificateForm()
        adress_form=AdressForm()
        formset = WarishFormSet(queryset=Person.objects.none())
        context['form']=form
        context['adress_form']=adress_form
        context['formset']=formset
        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        context={}
        form = CertificateForm(request.POST, request.FILES)


        if form.certificate_type == 9:
            formset = SamePersonFormSet(data=self.request.POST)
        else:
            formset = WarishFormSet(data=self.request.POST)

        adress_form = AdressForm(data=self.request.POST)
        certificate_types=CertificateType.objects.all().order_by('serial')
        context['certificate_types']=certificate_types
        license_types=LicenseType.objects.all().order_by('serial')
        context['license_types']=license_types
        certificate=Certificate.objects.filter(phone=request.POST.get('phone')).first()
        if certificate:
            if certificate.transaction == None:
                certificate.delete()
        tracking_no=gernerate_tracking_no()
        # Check if submitted forms are valid
        if form.is_valid():
            certificate=form.save(commit=False)
            person=None
            adress=None
            if adress_form.is_valid:
                adress=adress_form.save()
                certificate.adress=adress
                certificate.save()
            if formset.is_valid():
                person=formset.save()
                for person in person:
                    certificate.person.add(person)

            certificate.tracking_no=tracking_no
            chairman=Chairman.objects.all().order_by('-id').first()
            member=Member.objects.filter(ward=certificate.adress.village.ward).last()
            certificate.chairman=chairman
            certificate.member=member
            cause=Cause.objects.filter(id=request.POST.get('cause')).first()
            certificate.language=request.POST.get('language')
            certificate.passport=request.POST.get('passport')
            certificate.title=request.POST.get('title')
            certificate.amount=request.POST.get('amount')
            certificate.dob=request.POST.get('dob')
            certificate.date=request.POST.get('date')
            certificate.caste=request.POST.get('caste')
            certificate.cause=cause
            certificate.income=request.POST.get('income')
            certificate.profession=request.POST.get('profession')
            certificate.caste=request.POST.get('caste')
            certificate.description=request.POST.get('description')
            
            
            certificate.save()

            certificate=Certificate.objects.filter(tracking_no=tracking_no).first()

            context['certificate']=certificate
            return render(request,'certificate/applicant_details.html',context)

        
        return HttpResponse('nothing to see')



# class WarishanView(View):
#     model = WarishanCertificate
#     template_name = 'forms/certificate_form.html'
#     def get(self, request, *args, **kwargs):
#         context={}
#         form=WarishanCertificateForm()
#         adress_form=AdressForm()
#         form2=WarishForm()
#         formset = WarishFormSet(queryset=Person.objects.none())
#         context['form']=form
#         context['adress_form']=adress_form
#         context['form2']=form2
#         context['formset']=formset
#         return render(request,self.template_name, context)

#     def post(self, request, *args, **kwargs):
#         context={}
#         formset = WarishFormSet(data=self.request.POST)
#         form = WarishanCertificateForm(request.POST, request.FILES)
#         adress_form = AdressForm(data=self.request.POST)
#         tracking_no=gernerate_tracking_no()
#         print('language: ',request.POST.get('language'))
#         # Check if submitted forms are valid
#         if form.is_valid():
#             certificate=form.save(commit=False)
#             person=None
#             adress=None
#             if adress_form.is_valid:
#                 adress=adress_form.save()
#                 certificate.adress=adress
#                 certificate.save()
#             if formset.is_valid():
#                 person=formset.save()
#                 print(person)
#                 for person in person:
#                     certificate.person.add(person)
#                 #return HttpResponse('Form saved')
#             certificate.tracking_no=tracking_no
#             certificate.save()

#             certificate=WarishanCertificate.objects.filter(tracking_no=tracking_no).first()
#             context['certificate']=certificate
#             print("Certificate:",certificate)
#             return render(request,'certificate/applicant_details.html',context)

        
#         return HttpResponse('nothing to see')

class submitFormView(View):
    model = Certificate
    template_name = 'forms/applicant_details.html'
    def post(self, request, *args, **kwargs):
        certificate=Certificate.objects.filter(tracking_no=request.POST.get('tracking_no')).first()
        certificate_type=certificate.certificate_type
        payment_purpose=PaymentPurpose.objects.create(
                serial=certificate.id,
                certificate_type_id=certificate_type.id,
                title =certificate_type.name,
                payment_type_id=1,
                

            )
        return redirect(sslcommerz_payment_gateway(request, certificate, certificate_type,payment_purpose))
        


class DownloadCertificateView(View):
    model = Certificate
    template_name = 'certificate/download_certificate.html'
    def get(self, request, *args, **kwargs):
        context={}
        certificate_types=CertificateType.objects.all().order_by('serial')
        context['certificate_types']=certificate_types
        license_types=LicenseType.objects.all().order_by('serial')
        context['license_types']=license_types
        form=CertificateDownloadForm()
        context['form']=form
        return render(request,self.template_name, context)
    def post(self, request, *args, **kwargs):
        context={}
        certificate_types=CertificateType.objects.all().order_by('serial')
        context['certificate_types']=certificate_types
        license_types=LicenseType.objects.all().order_by('serial')
        context['license_types']=license_types
        certificate=Certificate.objects.filter(tracking_no=request.POST.get('tracking_no').strip(),certificate_type=request.POST.get('certificate_type')).first()
        transaction=Transaction.objects.filter(tracking_no=request.POST.get('tracking_no').strip()).first()
        if certificate:
            if transaction:
                if certificate.is_verified==False:
                    context['message']="আপনার আবেদনটি এখনো অনুমোদিত হয়নি, অপেক্ষা করুন"
                    form=CertificateDownloadForm()
                    context['form']=form
                    return render(request,self.template_name, context)
                

                certificate_type=certificate.certificate_type
                context['certificate']=certificate
                context['certificate_type']=certificate_type

                # if certificate.language == '2':
                #     return render(request,'certificate/en_certificate/en_'+certificate_type.template, context)
                # else:
                return render(request,'certificate/certificate/'+certificate_type.template, context)
            context['message']="দুখিঃত! আপনার সনদটির জন্য পেমেন্ট করা হয়নি"
            form=CertificateDownloadForm()
            context['form']=form
            return render(request,self.template_name, context)
        context['message']="দুখিঃত! সঠিক সনদ বাছাই করুন বা সঠিক ট্র্যাকিং নং প্রবেশ করান"
        form=CertificateDownloadForm()
        context['form']=form
        return render(request,self.template_name, context)
