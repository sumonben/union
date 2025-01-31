
import datetime
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import WarishanCertificate,Adress,Warish,CertificateType,Certificate,Cause
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
        exclude=['serial','name_en','email','transaction','is_verified','father_name_en','mother_name_en','tracking_no','adress','cause','warish','language']
    
            
        widgets = {
            'name': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  '','onkeypress' : "myFunction(this.id);",'label':'Village/house'}),
            'father_name': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  '','onkeypress' : "myFunction(this.id);",'label':'Street No.'}),
            'mother_name': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  '','onkeypress' : "myFunction(this.id);"}),
            'phone': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'মোবাইল নং','onkeypress' : "myFunction(this.id);"}),
            'nid': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'এনআইডি অথবা জন্ম নিবন্ধন','onkeypress' : "myFunction(this.id);"}),
    }
    def __init__(self, *args, **kwargs):
        self.certificate_type = kwargs.pop('instance', None)
        super(WarishanCertificateForm, self).__init__(*args, **kwargs)
        if self.certificate_type:
            self.fields['certificate_type']=forms.ModelChoiceField(label='সনদের ধরণ',queryset=CertificateType.objects.filter(id__in=[self.certificate_type.id,]),initial=CertificateType.objects.filter(id__in=[ self.certificate_type.id,]), widget=forms.Select( attrs={'class':'textfieldUSERinfo',}))
            if self.certificate_type.serial==3:
                self.fields['cause']=forms.ModelChoiceField(label='কারণ',queryset=Cause.objects.all(),initial=Cause.objects.filter(serial__in=[ 1,]), widget=forms.Select( attrs={'class':'textfieldUSERinfo',}))
            else:
                self.fields['cause']=forms.ModelChoiceField(label='',queryset=Cause.objects.all(), widget=forms.Select( attrs={'class':'textfieldUSERinfo','Hidden':True,}))

class WarishanCertificateForm(forms.ModelForm):
    class Meta:
        model = WarishanCertificate
        fields = "__all__"
        exclude=['serial','name_en','email','transaction','is_verified','father_name_en','mother_name_en','tracking_no','adress','warish','language']
    
            
        widgets = {
            'name': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  '','onkeypress' : "myFunction(this.id);",'label':'Village/house'}),
            'father_name': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  '','onkeypress' : "myFunction(this.id);",'label':'Street No.'}),
            'mother_name': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  '','onkeypress' : "myFunction(this.id);"}),
            'phone': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'মোবাইল নং','onkeypress' : "myFunction(this.id);"}),
            'nid': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'এনআইডি অথবা জন্ম নিবন্ধন','onkeypress' : "myFunction(this.id);"}),
            'cause': forms.Select(attrs={'class': 'textfieldUSER','onkeypress' : "myFunction(this.id);",'Hidden':True,}),
    }
    def __init__(self, *args, **kwargs):
        self.certificate_type = kwargs.pop('instance', None)
        super(WarishanCertificateForm, self).__init__(*args, **kwargs)
        if self.certificate_type:
            self.fields['certificate_type']=forms.ModelChoiceField(label='সনদের ধরণ',queryset=CertificateType.objects.filter(id__in=[self.certificate_type.id,]),initial=CertificateType.objects.filter(id__in=[ self.certificate_type.id,]), widget=forms.Select( attrs={'class':'textfieldUSERinfo',}))
            if self.certificate_type.serial==3:
                self.fields['cause']=forms.ModelChoiceField(label='কারণ',queryset=Cause.objects.all(),initial=Cause.objects.filter(serial__in=[ 1,]), widget=forms.Select( attrs={'class':'textfieldUSERinfo',}))
            else:
                self.fields['cause']=forms.ModelChoiceField(label='',queryset=Cause.objects.all(), widget=forms.Select( attrs={'class':'textfieldUSERinfo','Hidden':True,}))



class WarishForm(forms.ModelForm):
    class Meta:
        model = Warish
        fields = "__all__"
        exclude=['serial',]
        

class CertificateDownloadForm(forms.ModelForm):
    tracking_no= forms.CharField(label="ট্র্যাকিং নং-: ",required=True, widget=forms.TextInput(attrs={'class': 'textfieldUSERinfo',}))
    certificate_type= forms.ModelChoiceField(label="সার্টিফিকেটসমূহঃ ",required=True, queryset=CertificateType.objects.all(), widget=forms.Select(attrs={'class': 'textfieldUSERinfo',}))
    class Meta:
        model = Certificate
        fields = ['tracking_no','certificate_type']
        widgets = {
            'tracking_no': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'এনআইডি অথবা জন্ম নিবন্ধন','onkeypress' : "myFunction(this.id);",'required':True,}),
            'certificate_type': forms.Select(attrs={'class': 'textfieldUSER','onkeypress' : "myFunction(this.id);",'required':True,}),
    }



        
class AdressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = "__all__"
        exclude=['serial','holding_no','union','district','upazilla']
        widgets = {
            'village': forms.Select(attrs={'class': 'textfieldUSER','onkeypress' : "myFunction(this.id);",'label':'Village/house'}),
            'ward': forms.Select(attrs={'class': 'textfieldUSER','onkeypress' : "myFunction(this.id);",'label':'Street No.'}),
            'post_office': forms.Select(attrs={'class': 'textfieldUSER', 'onkeypress' : "myFunction(this.id);"}),
            
}
    


