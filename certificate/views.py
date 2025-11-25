from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Person,CertificateType,Certificate,Cause
from union.models import UnionDetails, ImportantLinks
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
from django.db.models import F



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
        important_links=ImportantLinks.objects.all().order_by('serial')
        context={}
        union_details=UnionDetails.objects.last()
        context['union_details']=union_details
        context['important_links']=important_links
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
        union_details=UnionDetails.objects.last()
        context['union_details']=union_details
        # certificate_types_first=CertificateType.objects.all().order_by('serial')[:4]
        certificate_types=CertificateType.objects.all().order_by('serial')
        license_types=LicenseType.objects.all().order_by('serial')
        chairman=Chairman.objects.filter(is_active=True).first()
        secretary=Secretary.objects.filter(is_active=True).first()
        member=Member.objects.all().order_by('-id').first() 
        context={}
        context['certificate_types']=certificate_types
        # context['certificate_types_first']=certificate_types_first
        context['license_types']=license_types
        context['chairman']=chairman
        context['secretary']=secretary
        context['member']=member
        context['member']=member
        return render(request,'contact.html',context)
    def post(self, request, *args, **kwargs):
        context={}
        return render(request,'home.html',context)


class HomeView(View):
    model = Certificate()
    template_name = 'home.html'
    def get(self, request, *args, **kwargs):
        context={}
        important_links=ImportantLinks.objects.all().order_by('serial')
        context['important_links']=important_links
        # certificate_types_first=CertificateType.objects.all().order_by('serial')[:4]
        chairman=Chairman.objects.filter(is_active=True).first()
        secretary=Secretary.objects.filter(is_active=True).order_by(F('serial').asc(nulls_last=True))
        members=Member.objects.filter(is_active=True).order_by(F('serial').asc(nulls_last=True))
        certificate_count1=Certificate.objects.filter(is_verified=True).count()
        certificate_count2=Certificate.objects.filter(is_verified=False).count()
        license_count1=License.objects.filter(is_verified=True).count()
        license_count2=License.objects.filter(is_verified=True).count()

        count=certificate_count1+license_count1
        context['chairman']=chairman
        context['secretary']=secretary
        context['members']=members
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
        form=CertificateForm(instance=certificate_type)
        form.certificate_type=certificate_type
        adress_form=AdressForm()
        context['form']=form
        context['adress_form']=adress_form
        if certificate_type.id== 1 or certificate_type.id== 7 or certificate_type.id== 28 or certificate_type.id== 29 :
            formset = WarishFormSet(queryset=Person.objects.none())
            context['formset']=formset
        if certificate_type.id== 9 or certificate_type.id == 15 or certificate_type.id == 25 or certificate_type.id == 10 or certificate_type.id == 26 :
            formset = SamePersonFormSet(queryset=Person.objects.none())
            context['formset']=formset
        

        
        return render(request,self.template_name,context)
    
    def post(self, request,id, *args, **kwargs):
        print('post: ',id)
        context={}
        return render(request,self.template_name,context)

    
class SelectCertificate(View):
    model = CertificateType()
    template_name = 'forms/certificate_form.html'
    def get(self, request, *args, **kwargs):
        context={}
        form=CertificateTypeForm()
        context['form']=form
        return render(request,'certificate/select_certificate.html',context)
    def post(self, request, *args, **kwargs):
        context={}
        certificate_type=CertificateType.objects.filter(id=request.POST.get('name')).first()
        context['certificate_type']=certificate_type
        form=CertificateForm(instance=certificate_type)
        form.certificate_type=certificate_type
        adress_form=AdressForm()
        context['form']=form
        context['adress_form']=adress_form
           
        if certificate_type.id== 1 or certificate_type.id== 7 or certificate_type.id== 28 or certificate_type.id== 29 :
            formset = WarishFormSet(queryset=Person.objects.none())
            context['formset']=formset
        if certificate_type.id== 9 or certificate_type.id == 15 or certificate_type.id == 25 or certificate_type.id == 10 or certificate_type.id == 26:
            formset = SamePersonFormSet(queryset=Person.objects.none())
            context['formset']=formset
                
         
        return render(request,self.template_name,context)
        

class CertificateView(View):
    model = Certificate
    template_name = 'forms/certificate_form.html'
    def get(self, request, *args, **kwargs):
        context={}
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
        certificate=Certificate.objects.filter(phone=request.POST.get('phone'), name=request.POST.get('name')).last()
        if certificate:
            if certificate.transaction is None:
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
                    person.tracking_no=tracking_no
                    person.save()
                    certificate.person.add(person)

            certificate.tracking_no=tracking_no
            chairman=Chairman.objects.filter(is_active=True).first()
            member=None
            member=Member.objects.filter(ward__name_en=certificate.adress.village.ward.name_en, is_active=True,is_preserved=False).last()
            if member is None:
                member=Member.objects.filter(ward__name_en=certificate.adress.village.ward.name_en, is_active=True).last()
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
            certificate.nid_file=request.FILES.get('nid_file')
            
            
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
        if certificate is not None:
            certificate_type=certificate.certificate_type
            payment_purpose=None
            payment_purpose=PaymentPurpose.objects.filter(certificate_type_id=certificate_type.id,payment_type_id=1).first()
            if payment_purpose:
                return redirect(sslcommerz_payment_gateway(request, certificate, certificate_type,payment_purpose))
            payment_purpose=PaymentPurpose.objects.create(
                    serial=0,
                    certificate_type_id=certificate_type.id,
                    title =certificate_type.name,
                    payment_type_id=1,
                    

                )
            return redirect(sslcommerz_payment_gateway(request, certificate, certificate_type,payment_purpose))

        return render(request, 'payment/alert.html')



class DownloadCertificateView(View):
    model = Certificate
    template_name = 'certificate/download_certificate.html'
    def get(self, request, *args, **kwargs):
        context={}
        form=CertificateDownloadForm()
        context['form']=form
        return render(request,self.template_name, context)
    def post(self, request, *args, **kwargs):
        context={}
        transaction=None
        certificate=Certificate.objects.filter(tracking_no=request.POST.get('tracking_no').strip(),certificate_type=request.POST.get('certificate_type')).first()
        context['certificate']=certificate
        if certificate:
            if certificate.transaction:
                transaction=Transaction.objects.filter(tracking_no=request.POST.get('tracking_no').strip(),id=certificate.transaction.id).first()
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

class DownloadApplicantsCopyView(View):
    model = Certificate
    template_name = 'certificate/download_applicants_copy.html'
    def get(self, request, *args, **kwargs):
        context={}
        form=CertificateDownloadForm()
        context['form']=form
        context['applicants_copy']='applicants_copy'
        return render(request,self.template_name, context)
    def post(self, request, *args, **kwargs):
        context={}
        transaction={}
        certificate=Certificate.objects.filter(tracking_no=request.POST.get('tracking_no').strip(),certificate_type=request.POST.get('certificate_type')).first()
        context['certificate']=certificate
        payment_type=PaymentType.objects.first()
        tran_purpose=PaymentPurpose.objects.filter(payment_type=payment_type).first()
        context['tran_purpose']=tran_purpose
        if certificate:
            if certificate.transaction:
                transaction=Transaction.objects.filter(tracking_no=request.POST.get('tracking_no').strip(),id=certificate.transaction.id).first()
                context['transaction']=transaction
        if certificate:
            if transaction:
                certificate_type=certificate.certificate_type
                context['certificate']=certificate
                context['certificate_type']=certificate_type

                # if certificate.language == '2':
                #     return render(request,'certificate/en_certificate/en_'+certificate_type.template, context)
                # else:

                return render(request,'payment/payment_reciept.html', context)
            context['message']="দুখিঃত! আপনার সনদটির জন্য পেমেন্ট করা হয়নি"
            form=CertificateDownloadForm()
            context['form']=form
            return render(request,self.template_name, context)
        context['message']="দুখিঃত! সঠিক সনদ বাছাই করুন বা সঠিক ট্র্যাকিং নং প্রবেশ করান"
        form=CertificateDownloadForm()
        context['form']=form
        return render(request,self.template_name, context)



class TutorialView(View):
    model = Certificate()
    template_name = 'certificate/tutorial.html'
    def get(self, request, *args, **kwargs):
        context={}
        return render(request,self.template_name, context)
