from django.http import HttpResponse
from django.shortcuts import render
from .models import PaymentPurpose
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.views.generic import View, TemplateView, DetailView
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse,HttpResponseNotFound
from .models import Transaction,PaymentPurpose
from region.models import UnionDetails
from .sslcommerz import sslcommerz_payment_gateway
from sslcommerz_lib import SSLCOMMERZ 
from django.contrib.auth import get_user_model
from certificate.models import Certificate,CertificateType 
from license.models import License,LicenseType

# Create your views here.
cradentials = {'store_id': 'israb672a4e32dfea5',
            'store_pass': 'israb672a4e32dfea5@ssl', 'issandbox': True} 
#cradentials = {'store_id': 'ictparkbd0live ',
#            'store_pass': '68045F6E0BDD747715', 'issandbox': False}

sslcommez = SSLCOMMERZ(cradentials)

class Index(TemplateView):
    template_name = "payment/index.html"

def DonateView(request):
    name = request.POST['name']
    amount = request.POST['amount']
    return redirect(sslcommerz_payment_gateway(request, name, amount))

def PaymentView(request,student,name,amount):
    name = request.POST['name']
    amount = request.POST['amount']
    return redirect(sslcommerz_payment_gateway(request, name, amount))


@method_decorator(csrf_exempt, name='dispatch')
class CheckoutSuccessView(View):
    model = Transaction
    template_name = 'payment/payment_reciept.html'
    
    def get(self, request, *args, **kwargs):
        return HttpResponse('Here! nothing to see')

    def post(self, request, *args, **kwargs):
        
        context={}
        data = self.request.POST
        print(data)
        id=int(data['value_d'])
        tran_purpose=PaymentPurpose.objects.filter(id=id).first()
        transaction=Transaction.objects.filter(tracking_no=data['value_a']).first()
        if transaction is None:
            try:
                transaction=Transaction.objects.create(
                    tracking_no=data['value_a'],
                    name = data['value_b'],
                    phone=data['value_c'],
                    email=data['value_d'],
                    tran_id=data['tran_id'],
                    tran_purpose=tran_purpose,
                    val_id=data['val_id'],
                    amount=data['amount'],
                    card_type=data['card_type'],
                    card_no=data['card_no'],
                    store_amount=data['store_amount'],
                    bank_tran_id=data['bank_tran_id'],
                    status=data['status'],
                    tran_date=data['tran_date'],
                    currency=data['currency'],
                    card_issuer=data['card_issuer'],
                    card_brand=data['card_brand'],
                    card_issuer_country=data['card_issuer_country'],
                    card_issuer_country_code=data['card_issuer_country_code'],
                    verify_sign=data['verify_sign'],
                    verify_sign_sha2=data['verify_sign_sha2'],
                    currency_rate=data['currency_rate'],
                    risk_title=data['risk_title'],
                    risk_level=data['risk_level'],

                )
                
                
                messages.success(request,'Payment Successful!!')
                
            except:
                messages.success(request,'Something Went Wrong')
                context['messages']=messages    
            
        if tran_purpose.payment_type.id == 1:
                    certificate=Certificate.objects.filter(tracking_no=data['value_a']).first()
                    year=transaction.created_at.year
                    if certificate.memorial_no is None:
                        count=Transaction.objects.filter(tran_purpose__certificate_type_id=tran_purpose.certificate_type_id,tran_purpose__payment_type=tran_purpose.payment_type).filter(created_at__year=year).count()
                        memorial_no='3813.04.'+str(tran_purpose.payment_type.id).zfill(2)+str(tran_purpose.certificate_type_id).zfill(2)+'/'+str(year)+'('+str(count)+')'
                        certificate.memorial_no=memorial_no
                    context['certificate']=certificate
                    context['certificate_type']=certificate.certificate_type
                   
                    certificate.transaction=transaction
                    certificate.save()
        else:
                    license=License.objects.filter(tracking_no=data['value_a']).first()
                    if license.memorial_no is None:
                        year=transaction.created_at.year
                        count=Transaction.objects.filter(tran_purpose__certificate_type_id=tran_purpose.certificate_type_id,tran_purpose__payment_type=tran_purpose.payment_type).filter(created_at__year=year).count()
                        memorial_no='3813.04.'+str(tran_purpose.payment_type.id).zfill(2)+str(tran_purpose.certificate_type_id).zfill(2)+'/'+str(year)+'('+str(count)+')'
                        license_no=str(tran_purpose.payment_type.id).zfill(2)+'-'+str(tran_purpose.certificate_type_id).zfill(2)+'-'+str(year).zfill(2)+'-'+str(count)
                        license.license_no=license_no
                        license.memorial_no=memorial_no
                    context['license']=license
                    context['license_type']=license.license_type
                    
                    license.transaction=transaction
                    license.save()
                
        union_details=UnionDetails.objects.last()
        context['union_details']=union_details
        context['transaction']=transaction
        context['tran_purpose']=tran_purpose
                
        return render(request,self.template_name,context)
        

@method_decorator(csrf_exempt, name='dispatch')
class CheckoutIPNView(View):
    model = Transaction
    template_name = 'payment/payment_receipt.html'
    
    def get(self, request, *args, **kwargs):
        return HttpResponse('nothing to see')

    def post(self, request, *args, **kwargs):
        
        context={}
        name_of_payee=None
        data = self.request.POST
        post_body={}
        tran_purpose=PaymentPurpose.objects.filter(id=data['value_d']).first()
        if tran_purpose:
             if tran_purpose.payment_type.id == 1:
                certificate=Certificate.objects.filter(tracking_no=data['value_a']).first()
                name_of_payee=certificate.name
             else:
                certificate=License.objects.filter(tracking_no=data['value_a']).first()
                name_of_payee=certificate.license_owner_name

        # print(tran_purpose)
        if data['status'] == 'VALID':
            # print("Yes")
            post_body['val_id'] = data['val_id']
            # print("Validation prev: ",post_body['val_id'])
            response = sslcommez.validationTransactionOrder(post_body['val_id'])
            # print("Validation: ",response)
            transaction=Transaction.objects.create(
                tracking_no=data['value_a'],
                name =name_of_payee,
                phone=data['value_c'],
                email=data['value_d'],
                tran_id=data['tran_id'],
                tran_purpose=tran_purpose,
                val_id=data['val_id'],
                amount=data['amount'],
                card_type=data['card_type'],
                card_no=data['card_no'],
                store_amount=data['store_amount'],
                bank_tran_id=data['bank_tran_id'],
                status=data['status'],
                tran_date=data['tran_date'],
                currency=data['currency'],
                card_issuer=data['card_issuer'],
                card_brand=data['card_brand'],
                card_issuer_country=data['card_issuer_country'],
                card_issuer_country_code=data['card_issuer_country_code'],
                verify_sign=data['verify_sign'],
                verify_sign_sha2=data['verify_sign_sha2'],
                currency_rate=data['currency_rate'],
                risk_title=data['risk_title'],
                risk_level=data['risk_level'],

            )
            
        else:
            transaction=Transaction.objects.create(
                            tracking_no=data['value_a'],
                            name = data['value_b'],
                            phone=data['value_c'],
                            email=data['value_d'],
                            tran_id=data['tran_id'],
                            tran_purpose=tran_purpose,
                            val_id="None",
                            amount=data['amount'],
                            card_type=data['card_type'],
                            card_no=data['card_no'],
                            store_amount=0,
                            bank_tran_id=data['bank_tran_id'],
                            status=data['status'],
                            tran_date=data['tran_date'],
                            currency=data['currency'],
                            card_issuer=data['card_issuer'],
                            card_brand=data['card_brand'],
                            card_issuer_country=data['card_issuer_country'],
                            card_issuer_country_code=data['card_issuer_country_code'],
                            verify_sign=data['verify_sign'],
                            verify_sign_sha2=data['verify_sign_sha2'],
                            currency_rate=data['currency_rate'],
                            risk_title='None',
                            risk_level='0',
            
                        )            
        
        messages.success(request,'Something Went Wrong')
        context['messages']=messages
        return redirect('/')


@method_decorator(csrf_exempt, name='dispatch')
class CheckoutFaildView(View):
    template_name = 'payment/failed.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        context={}
        data = self.request.POST
        print(self.request.POST)
        id=int(data['value_d'])
        tran_purpose=PaymentPurpose.objects.filter(id=id).first()
        
        if tran_purpose.payment_type.id == 1:
                    certificate=Certificate.objects.filter(tracking_no=data['value_a']).first()
                    context['certificate']=certificate
                    context['certificate_type']=certificate.certificate_type
                    certificate.delete()
                   
                    
        else:
                    license=License.objects.filter(tracking_no=data['value_a']).first()
                    license.delete()
                    context['license']=license
                    context['license_type']=license.license_type
                    
                    
                
               
        context['tran_purpose']=tran_purpose
                
        return render(request,self.template_name,context)
            
        
@method_decorator(csrf_exempt, name='dispatch')
class CheckoutCanceledView(View):
    template_name = 'payment/canceled.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        context={}
        data = self.request.POST

        id=int(data['value_d'])
        tran_purpose=PaymentPurpose.objects.filter(id=id).first()
        
        if tran_purpose.payment_type.id == 1:
                    certificate=Certificate.objects.filter(tracking_no=data['value_a']).first()
                    context['certificate']=certificate
                    context['certificate_type']=certificate.certificate_type
                    certificate.delete()
                   
                    
        else:
                    license=License.objects.filter(tracking_no=data['value_a']).first()
                    license.delete()
                    context['license']=license
                    context['license_type']=license.license_type
                    
                    
                
               
        context['tran_purpose']=tran_purpose
                
        return render(request,self.template_name,context)
    


def searchPayment(request):
    context={}
    flag1=0
    flag2=0
    
    if request.method=='POST':
        
        student=Certificate.objects.filter(class_roll=request.POST.get('roll').strip()).first()
        subject_choice=Certificate.objects.filter(class_roll=request.POST.get('roll').strip()).first()
        purpose=PaymentPurpose.objects.filter(id=request.POST.get('purpose'),is_active=True).first()
        if student:
            #print(student,purpose)

            context['student']=student
            context['purpose']=purpose
            
            #return render(request, 'payment/search_payment.html', context=context)

            return render(request, 'payment/check_payment_info.html', context=context)

        
        
    form=()
    context['form']=form
    return render(request, 'payment/search_payment.html', context=context)


def ProceedPayment(request):
    context={}

    if request.method=='POST':

        student=Certificate.objects.filter(id=request.POST.get('student')).first()

        purpose=PaymentPurpose.objects.filter(id=request.POST.get('purpose'),is_active=True).first()
        if student:
            return redirect(sslcommerz_payment_gateway(request, student, purpose))

        
        
    form=()
    context['form']=form
    return render(request, 'payment/search_payment.html', context=context)
