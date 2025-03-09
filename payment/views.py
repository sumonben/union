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
from .sslcommerz import sslcommerz_payment_gateway
from sslcommerz_lib import SSLCOMMERZ 
from django.contrib.auth import get_user_model
from certificate.models import Certificate,CertificateType 
from license.models import License,LicenseType

# Create your views here.
cradentials = {'store_id': 'israb672a4e32dfea5',
            'store_pass': 'israb672a4e32dfea5@ssl', 'issandbox': True} 
            
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
        transaction=None
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
            #print("data['value_d']:",tran_purpose.payment_type)
            if transaction:
                if tran_purpose.payment_type.id == 1:
                    certificate=Certificate.objects.filter(tracking_no=data['value_a']).first()
                    context['certificate']=certificate
                    context['certificate_type']=certificate.certificate_type
                   
                    certificate.transaction=transaction
                    certificate.save()
                else:
                    license=License.objects.filter(tracking_no=data['value_a']).first()
                    context['license']=license
                    context['license_type']=license.license_type
                    
                    license.transaction=transaction
                    license.save()
                
               
                context['transaction']=transaction
                context['tran_purpose']=tran_purpose
                
                return render(request,self.template_name,context)
            # if tran_purpose.payment_type.id == 2:
            #     #print("data['value_d']:",tran_purpose.payment_type)
            #     student=Certificate.objects.filter(class_roll=data['value_a']).first()
            #     #print(student)
            #     context['transaction']=transaction
            #     context['purpose']=tran_purpose
            #     context['certificate']=certificate
            #     return render(request,self.template_name,context)

            
            messages.success(request,'Payment Successful!!')
            
        except:
            messages.success(request,'Something Went Wrong')
            context['messages']=messages
        return render(request,self.template_name,context)




@method_decorator(csrf_exempt, name='dispatch')
class CheckoutFaildView(View):
    template_name = 'payment/failed.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        data=request.POST
        context={}
        tran_purpose=PaymentPurpose.objects.filter(id=data['value_d']).first()
        context['tran_purpose']=tran_purpose
        
        if tran_purpose.payment_type.id == 2:
                print("data['value_d']:",tran_purpose.payment_type)
                student=Certificate.objects.filter(class_roll=data['value_a']).first()
                #print(student)
                context['purpose']=tran_purpose
                context['student']=student
                form=()
                context['form']=form
                message='Payment Failed'
                context['message']=message
                
                return render(request,self.template_name,context)
        if tran_purpose.payment_type.id == 3:
                #print("data['value_d']:",tran_purpose.payment_type)
                student=Certificate.objects.filter(class_roll=data['value_a']).first()
                #print(student)
                context['purpose']=tran_purpose
                context['student']=student
                message='Payment Failed'
                context['message']=message
                form=()
                context['form']=form
                return render(request,self.template_name,context)

        if tran_purpose.payment_type.id == 1:
                
                students=Certificate.objects.filter(phone=data['value_b'],user=None)
                for std in students:
                    std.delete()

                #print(student)
                context['purpose']=tran_purpose
                context['student']=student
                message='Payment Failed'
                context['message']=message
        
        form=()
        context['form']=form  
        message='Payment Failed'
        context['message']=message
        return render(request,self.template_name,context)

@method_decorator(csrf_exempt, name='dispatch')
class CheckoutCanceledView(View):
    template_name = 'payment/search_payment.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        data=request.POST
        context={}
        tran_purpose=PaymentPurpose.objects.filter(id=data['value_d']).first()
        context['tran_purpose']=tran_purpose
        messages.success(request,'Payment Canceled')
        context['messages']=messages
        
        if tran_purpose.payment_type.id == 2:
                print("data['value_d']:",tran_purpose.payment_type)
                student=Certificate.objects.filter(class_roll=data['value_a']).first()
                #print(student)
                context['purpose']=tran_purpose
                context['student']=student
                form=()
                context['form']=form
                message='Payment Canceled'
                context['message']=message
                
                return render(request,self.template_name,context)
        if tran_purpose.payment_type.id == 3:
                #print("data['value_d']:",tran_purpose.payment_type)
                student=Certificate.objects.filter(class_roll=data['value_a']).first()
                #print(student)
                context['purpose']=tran_purpose
                context['student']=student
                message='Payment Canceled'
                context['message']=message
                form=()
                context['form']=form
                return render(request,self.template_name,context)

        if tran_purpose.payment_type.id == 1:
                
                students=Certificate.objects.filter(phone=data['value_b'],user=None)
                for std in students:
                    std.delete()

                #print(student)
                context['purpose']=tran_purpose
                context['student']=student
                message='Payment Canceled'
                context['message']=message
        
        form=()
        context['form']=form  
        message='Payment Canceled'
        context['message']=message
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
