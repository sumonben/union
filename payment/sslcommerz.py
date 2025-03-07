import string
import random
from django.conf import settings
from sslcommerz_lib import SSLCOMMERZ
from .models import PaymentGateway


def generator_trangection_id( size=10, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


    

def sslcommerz_payment_gateway(request, certificate,certificate_type, type):
    
    print(certificate,certificate_type)
    gateway = PaymentGateway.objects.all().first()
    cradentials = {'store_id': 'israb672a4e32dfea5',
            'store_pass': 'israb672a4e32dfea5@ssl', 'issandbox': True} 
    
    '''cradentials = {'store_id': 'gmrwcedubdlive',
            'store_pass': '677CD7B61AB5A81511', 'issandbox': False} '''
    
    sslcommez = SSLCOMMERZ(cradentials)
    body = {}
    body['certificate'] = certificate
    body['total_amount'] = certificate_type.amount
    body['currency'] = "BDT"
    body['tran_id'] = generator_trangection_id()
    body['success_url'] = 'http://localhost:8000/payment/success/'
    body['fail_url'] = 'http://localhost:8000/payment/payment/failed/'
    body['cancel_url'] = 'http://localhost:8000/payment/canceled/'
    body['emi_option'] = 0
    if type == 1:
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
    if type == 1:
       body['value_b'] =certificate.name 
    else:
        body['value_b'] = certificate.license_owner_name
    body['value_c'] = certificate.phone
    body['value_d'] = type
    
    


    response = sslcommez.createSession(body)
    #print(response)   
    #return  response["GatewayPageURL"]
    return 'https://sandbox.sslcommerz.com/gwprocess/v4/gw.php?Q=pay&SESSIONKEY=' + response["sessionkey"]
    return 'https://securepay.sslcommerz.com/gwprocess/v4/api.php?Q=pay&SESSIONKEY=' + response["sessionkey"]

