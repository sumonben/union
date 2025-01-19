from django.http import HttpResponse
from django.shortcuts import render
from .models import WarishanCertificate
from .forms import WarishanCertificateForm,AdressForm,WarishForm
from django.contrib.auth.decorators import login_required
from django.views.generic import View
# Create your views here.

def SelectCertificate(request):
    return render(request,'certificate/select_certificate.html',)

class WarishanView(View):
    model = WarishanCertificate
    template_name = 'forms/warishan_form.html'
    def get(self, request, *args, **kwargs):
        context={}
        form=WarishanCertificateForm()
        form1=AdressForm()
        form2=WarishForm()
        context['form']=form
        context['form1']=form1
        context['form2']=form2
        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        return HttpResponse('nothing to see')
