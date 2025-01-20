
import datetime
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import WarishanCertificate,Adress,Warish
from django.forms import modelformset_factory

'''class SearchPaymentForm(forms.ModelForm):
    roll= forms.CharField(widget=forms.TextInput(attrs={'class': 'textfieldUSERinfo','onchange' : 'myFunction(this.id)',}))
    purpose= forms.ModelChoiceField(required=True,queryset=PaymentPurpose.objects.filter(is_active=True),widget=forms.Select(attrs={'class': 'textfieldUSERinfo',}))

    class Meta:
        model = PaymentPurpose
        fields = []
'''
WarishFormSet = modelformset_factory(
    Warish, fields=("name", "relation"), extra=1,
    widgets = {
            'name': forms.TextInput(attrs={'class': 'textfieldUSER',}),
            'relation': forms.Select(attrs={'class': 'textfieldUSER',}),            
        }
)
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
        exclude=['serial','holding_no',]
        widgets = {
            'village': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'Village Name/house No.','onkeypress' : "myFunction(this.id);",'label':'Village/house'}),
            'word_no': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'Street Name/No.','onkeypress' : "myFunction(this.id);",'label':'Street No.'}),
            'post_office': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'Bogura-5800','onkeypress' : "myFunction(this.id);"}),
            'union': forms.Select(attrs={'class': 'textfieldUSER',}),
            'district': forms.Select(attrs={'class': 'textfieldUSER',}),            
            'upazilla': forms.Select(attrs={'class': 'textfieldUSER',}),


        }
    


