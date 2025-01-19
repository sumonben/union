
import datetime
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import WarishanCertificate,Adress,Warish

'''class SearchPaymentForm(forms.ModelForm):
    roll= forms.CharField(widget=forms.TextInput(attrs={'class': 'textfieldUSERinfo','onchange' : 'myFunction(this.id)',}))
    purpose= forms.ModelChoiceField(required=True,queryset=PaymentPurpose.objects.filter(is_active=True),widget=forms.Select(attrs={'class': 'textfieldUSERinfo',}))

    class Meta:
        model = PaymentPurpose
        fields = []
'''

class WarishanCertificateForm(forms.ModelForm):
    class Meta:
        model = WarishanCertificate
        fields = "__all__"
        exclude=['serial','name_en','email','transaction','is_verified','certificate_type','father_name_en','mother_name_en','tracking_no','adress','warish']
class WarishForm(forms.ModelForm):
    class Meta:
        model = Warish
        fields = "__all__"
        exclude=['serial',]
class AdressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = "__all__"
        exclude=['serial',]
