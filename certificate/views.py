from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Person,CertificateType,Certificate,Cause
from payment.models import Transaction
from account.models import Chairman, Member
from .forms import AdressForm,WarishFormSet,WarishForm,CertificateTypeForm,CertificateForm,CertificateDownloadForm
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.forms import formset_factory
from payment.sslcommerz import sslcommerz_payment_gateway

import string
import random
# Create your views here.

def gernerate_tracking_no( size=8, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


class FrontView(View):
    model = Certificate()
    template_name = 'front.html'
    def get(self, request, *args, **kwargs):
        certificate_type=CertificateType.objects.all().order_by('serial')
        context={}
        context['certificate_type']=certificate_type
        return render(request,'front.html',context)
    def post(self, request, *args, **kwargs):
        context={}
        return render(request,'front.html',context)

class HomeView(View):
    model = Certificate()
    template_name = 'home.html'
    def get(self, request, *args, **kwargs):
        certificate_type=CertificateType.objects.all().order_by('serial')
        context={}
        context['certificate_type']=certificate_type        
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
        form2=WarishForm()
        formset = WarishFormSet(queryset=Person.objects.none())
        context['form']=form
        context['adress_form']=adress_form
        if certificate_type.id== 1:
            context['form2']=form2
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
        print(request.POST.get('name'))
        certificate_type=CertificateType.objects.filter(id=request.POST.get('name')).first()
        context['certificate_type']=certificate_type
        form=CertificateForm(instance=certificate_type)
        form.certificate_type=certificate_type
        adress_form=AdressForm()
        form2=WarishForm()
        formset = WarishFormSet(queryset=Person.objects.none())
        context['form']=form
        context['adress_form']=adress_form
        if certificate_type.id== 1:
            context['form2']=form2
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

        formset = WarishFormSet(data=self.request.POST)
        form = CertificateForm(request.POST, request.FILES)
        print(form.certificate_type)
        adress_form = AdressForm(data=self.request.POST)
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
                print(person)
                for person in person:
                    certificate.person.add(person)
                #return HttpResponse('Form saved')
            certificate.tracking_no=tracking_no
            chairman=Chairman.objects.all().order_by('-id').first()
            member=Member.objects.filter(ward=certificate.adress.village.ward).last()
            certificate.chairman=chairman
            certificate.member=member
            cause=Cause.objects.filter(id=request.POST.get('cause')).first()
            certificate.language=request.POST.get('language')
            certificate.cause=cause
            certificate.income=request.POST.get('income')
            certificate.profession=request.POST.get('profession')
            certificate.caste=request.POST.get('caste')
            
            certificate.save()

            certificate=Certificate.objects.filter(tracking_no=tracking_no).first()

            context['certificate']=certificate
            print("Certificate:",certificate)
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
        return redirect(sslcommerz_payment_gateway(request, certificate, certificate_type))

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
        certificate=Certificate.objects.filter(tracking_no=request.POST.get('tracking_no'),certificate_type=request.POST.get('certificate_type')).first()
        transaction=Transaction.objects.filter(tracking_no=request.POST.get('tracking_no')).first()
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

                if certificate_type.serial == 2:
                    return render(request,'certificate/certificate/warishan_certificate.html', context)
                return render(request,'certificate/certificate/citizenship_certificate.html', context)
            context['message']="দুখিঃত! আপনার সনদটির জন্য পেমেন্ট করা হয়নি"
            form=CertificateDownloadForm()
            context['form']=form
            return render(request,self.template_name, context)
        context['message']="দুখিঃত! সঠিক সনদ বাছাই করুন বা সঠিক ট্র্যাকিং নং প্রবেশ করান"
        form=CertificateDownloadForm()
        context['form']=form
        return render(request,self.template_name, context)
