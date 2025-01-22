
import datetime
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import WarishanCertificate,Adress,Warish,CertificateType,Certificate
from django.forms import modelformset_factory

'''class SearchPaymentForm(forms.ModelForm):
    roll= forms.CharField(widget=forms.TextInput(attrs={'class': 'textfieldUSERinfo','onchange' : 'myFunction(this.id)',}))
    purpose= forms.ModelChoiceField(required=True,queryset=PaymentPurpose.objects.filter(is_active=True),widget=forms.Select(attrs={'class': 'textfieldUSERinfo',}))

    class Meta:
        model = PaymentPurpose
        fields = []
'''
        


WarishFormSet = modelformset_factory(
    Warish, fields=("name", "relation","comment"), extra=1,
    widgets = {
            'name': forms.TextInput(attrs={'class': 'textfieldUSER',}),
            'relation': forms.Select(attrs={'class': 'textfieldUSER',}),            
            'comment': forms.Select(attrs={'class': 'textfieldUSER',}),            
        }
)

class CertificateTypeForm(forms.ModelForm):
    name= forms.ModelChoiceField(label="সার্টিফিকেটসমূহঃ ",required=True,queryset=CertificateType.objects.all(),widget=forms.Select(attrs={'class': 'textfieldUSERinfo',}))
    class Meta:
        model = CertificateType
        fields = []

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = "__all__"
        exclude=['serial','name_en','email','transaction','is_verified','certificate_type','father_name_en','mother_name_en','tracking_no','adress','warish']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  '','onkeypress' : "myFunction(this.id);",'label':'Village/house'}),
            'father_name': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  '','onkeypress' : "myFunction(this.id);",'label':'Street No.'}),
            'mother_name': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  '','onkeypress' : "myFunction(this.id);"}),
            'phone': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'মোবাইল নং','onkeypress' : "myFunction(this.id);"}),
            'nid': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'এনআইডি অথবা জন্ম নিবন্ধন','onkeypress' : "myFunction(this.id);"}),
            


        }

class WarishanCertificateForm(forms.ModelForm):
    class Meta:
        model = WarishanCertificate
        fields = "__all__"
        exclude=['serial','name_en','email','transaction','is_verified','certificate_type','father_name_en','mother_name_en','tracking_no','adress','warish']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  '','onkeypress' : "myFunction(this.id);",'label':'Village/house'}),
            'father_name': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  '','onkeypress' : "myFunction(this.id);",'label':'Street No.'}),
            'mother_name': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  '','onkeypress' : "myFunction(this.id);"}),
            'phone': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'মোবাইল নং','onkeypress' : "myFunction(this.id);"}),
            'nid': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'এনআইডি অথবা জন্ম নিবন্ধন','onkeypress' : "myFunction(this.id);"}),
            


        }
class WarishForm(forms.ModelForm):
    class Meta:
        model = Warish
        fields = "__all__"
        exclude=['serial',]
        

        
class AdressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = "__all__"
        exclude=['serial','holding_no','union','district','upazilla']
        widgets = {
            'village': forms.Select(attrs={'class': 'textfieldUSER','onkeypress' : "myFunction(this.id);",'label':'Village/house'}),
            'word': forms.Select(attrs={'class': 'textfieldUSER','onkeypress' : "myFunction(this.id);",'label':'Street No.'}),
            'post_office': forms.Select(attrs={'class': 'textfieldUSER', 'onkeypress' : "myFunction(this.id);"}),
            


        }
    


