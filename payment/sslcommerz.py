import string
import random
from django.conf import settings
from sslcommerz_lib import SSLCOMMERZ
from .models import PaymentGateway,PaymentPurpose,PaymentType

def generator_trangection_id( size=10, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


    

def sslcommerz_payment_gateway(request, certificate,certificate_type, payment_purpose):
    
    gateway = PaymentGateway.objects.all().first()
    cradentials = {'store_id': 'israb672a4e32dfea5',
            'store_pass': 'israb672a4e32dfea5@ssl', 'issandbox': True} 
    
    #cradentials = {'store_id': 'ictparkbd0live',
    #       'store_pass': '68045F6E0BDD747715', 'issandbox': False}
    sslcommez = SSLCOMMERZ(cradentials)
    body = {}
    body['certificate'] = certificate
    body['total_amount'] = certificate_type.amount
    body['currency'] = "BDT"
    body['tran_id'] = generator_trangection_id()
    body['success_url'] ='https://' +str(request.META['HTTP_HOST'])+'/payment/success/'
    body['fail_url'] = 'https://' +str(request.META['HTTP_HOST'])+'/payment/failed/'
    body['cancel_url'] = 'https://' +str(request.META['HTTP_HOST'])+'/payment/canceled/'
    body['ipn_url'] = 'https://' +str(request.META['HTTP_HOST'])+'/payment/ipn/'
    body['emi_option'] = 0
    if payment_purpose.payment_type.id == 1:
        body['cus_name'] = certificate.name
    else:
        body['cus_name'] = certificate.licensed_name
    body['cus_email'] = 'request.data["email"]'
    if certificate.phone:
        body['cus_phone'] = certificate.phone
    else:
        body['cus_phone'] = '01712539569'
    body['cus_add1'] = 'request.data["address"]'
    body['cus_city'] = 'request.data["address"]'
    body['cus_country'] = 'Bangladesh'
    body['shipping_method'] = "NO"
    body['multi_card_name'] = ""
    body['num_of_item'] = 1
    body['product_name'] = "Test"
    body['product_category'] = "Test Category"
    body['product_profile'] = "general"
    body['value_a'] = certificate.tracking_no
    if payment_purpose.payment_type.id == 1:
       body['value_b'] =certificate.name 
    else:
        body['value_b'] = certificate.license_owner_name
    body['value_c'] = certificate.phone
    body['value_d'] = payment_purpose.id
    
    


    response = sslcommez.createSession(body)
    #print(response)   
    return  response["GatewayPageURL"]
    return 'https://sandbox.sslcommerz.com/gwprocess/v4/gw.php?Q=pay&SESSIONKEY=' + response["sessionkey"]
    return 'https://securepay.sslcommerz.com/gwprocess/v4/api.php?Q=pay&SESSIONKEY=' + response["sessionkey"]

def sslcommerz_payment_gateway_holdingtax(request, holding_tax,holding_type, payment_purpose):
    
    gateway = PaymentGateway.objects.all().first()
    cradentials = {'store_id': 'israb672a4e32dfea5',
            'store_pass': 'israb672a4e32dfea5@ssl', 'issandbox': True} 
    
    #cradentials = {'store_id': 'ictparkbd0live',
    #       'store_pass': '68045F6E0BDD747715', 'issandbox': False}
    sslcommez = SSLCOMMERZ(cradentials)
    body = {}
    body['holding_tax'] = holding_tax
    body['total_amount'] = holding_tax.amount
    body['currency'] = "BDT"
    body['tran_id'] = generator_trangection_id()
    body['success_url'] ='https://' +str(request.META['HTTP_HOST'])+'/payment/success/'
    body['fail_url'] = 'https://' +str(request.META['HTTP_HOST'])+'/payment/failed/'
    body['cancel_url'] = 'https://' +str(request.META['HTTP_HOST'])+'/payment/canceled/'
    body['ipn_url'] = 'https://' +str(request.META['HTTP_HOST'])+'/payment/ipn/'
    body['emi_option'] = 0
    body['cus_name'] = holding_tax.name
    body['cus_email'] = 'request.data["email"]'
    body['cus_phone'] = holding_tax.phone
    body['cus_add1'] = 'request.data["address"]'
    body['cus_city'] = 'request.data["address"]'
    body['cus_country'] = 'Bangladesh'
    body['shipping_method'] = "NO"
    body['multi_card_name'] = ""
    body['num_of_item'] = 1
    body['product_name'] = "Test"
    body['product_category'] = "Test Category"
    body['product_profile'] = "general"
    body['value_a'] = holding_tax.holding_no
    body['value_b'] =holding_tax.fiscal_year.id 
    body['value_c'] = holding_tax.phone
    body['value_d'] = payment_purpose.id
    
    


    response = sslcommez.createSession(body)
    #print(response)   
    return  response["GatewayPageURL"]
    return 'https://sandbox.sslcommerz.com/gwprocess/v4/gw.php?Q=pay&SESSIONKEY=' + response["sessionkey"]
    return 'https://securepay.sslcommerz.com/gwprocess/v4/api.php?Q=pay&SESSIONKEY=' + response["sessionkey"]
