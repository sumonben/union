from django.http import HttpResponse
from django.shortcuts import render
from .models import WarishanCertificate,Warish
from .forms import WarishanCertificateForm,AdressForm,WarishFormSet,WarishForm
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.forms import formset_factory

# Create your views here.

def SelectCertificate(request):
    return render(request,'certificate/select_certificate.html',)

class WarishanView(View):
    model = WarishanCertificate
    template_name = 'forms/warishan_form.html'
    def get(self, request, *args, **kwargs):
        context={}
        form=WarishanCertificateForm()
        adress_form=AdressForm()
        form2=WarishForm()
        formset = WarishFormSet(queryset=Warish.objects.none())
        context['form']=form
        context['adress_form']=adress_form
        context['form2']=form2
        context['formset']=formset
        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        return HttpResponse('nothing to see')
