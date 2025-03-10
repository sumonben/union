
import datetime
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Adress,Person,CertificateType,Certificate,Cause
from django.forms import modelformset_factory
from django.contrib.admin.widgets import AdminDateWidget
COMMENT_CHOICE={
    '0':'------',
    '1':'বর্তমানে মৃত',

}

LANGUAGE_CHOICE={
    '1':'বাংলা',
    '2':'English',

}
AMOUNT_CHOICE={
    '0':'------',
    '1':'০',
    '2':'১',
    '3':'২',
    '4':'৩',
    '5':'৪',
    '6':'৫',
    '7':'৬',
    '8':'৭',
    '9':'৮',
    '10':'৯',
    '11':'১০',
    

}

'''class SearchPaymentForm(forms.ModelForm):
    roll= forms.CharField(widget=forms.TextInput(attrs={'class': 'textfieldUSERinfo','onchange' : 'myFunction(this.id)',}))
    purpose= forms.ModelChoiceField(required=True,queryset=PaymentPurpose.objects.filter(is_active=True),widget=forms.Select(attrs={'class': 'textfieldUSERinfo',}))

    class Meta:
        model = PaymentPurpose
        fields = []
'''
        


WarishFormSet = modelformset_factory(
    Person, fields=("name", "relation","comment"), extra=1,
    widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-sm',}),
            'relation': forms.Select(attrs={'class': 'form-control form-control-sm',}),            
            'comment': forms.Select(choices=COMMENT_CHOICE,attrs={'class': 'form-control form-control-sm',}),            
        }
)
SamePersonFormSet = modelformset_factory(
    Person, fields=("name",), extra=1,
    widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-sm',}),
                  }
)

class CertificateTypeForm(forms.ModelForm):
    name= forms.ModelChoiceField(label="সার্টিফিকেটসমূহঃ ",required=True,queryset=CertificateType.objects.all(),widget=forms.Select(attrs={'class': 'form-control form-control-sm',}))
    class Meta:
        model = CertificateType
        fields = []

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = "__all__"
        exclude=['serial','name_en','transaction','is_verified','father_name_en','mother_name_en','passport','tracking_no','adress','dob','description','cause','amount','date','person','chairman','member','caste','income','profession','language']
    
            
        
    def __init__(self, *args, **kwargs):
        self.certificate_type = kwargs.pop('instance', None)
        super(CertificateForm, self).__init__(*args, **kwargs)
        self.fields['name']=forms.CharField(label='নাম', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'নাম লিখুন'}))
        self.fields['phone']=forms.CharField(label='মোবাইল', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'ie: 01*********'}))
        self.fields['email']=forms.CharField(label='ই-মেইল', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'ie: *****@***.com'}))
        self.fields['nid']=forms.CharField(required=False,label='জাতীয় পরিচয়/জন্ম নিবন্ধন', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'না থাকলে প্রয়োজন নেই'}))
        self.fields['father_name']=forms.CharField(label='বাবার নাম', widget=forms.TextInput( attrs={'class':'form-control form-control-sm',}))
        self.fields['mother_name']=forms.CharField(label='মায়ের নাম', widget=forms.TextInput( attrs={'class':'form-control form-control-sm',}))

        if self.certificate_type:
            self.fields['certificate_type']=forms.ModelChoiceField(label='সনদের ধরণ',queryset=CertificateType.objects.filter(id__in=[self.certificate_type.id,]),initial=CertificateType.objects.filter(id__in=[ self.certificate_type.id,]), widget=forms.Select( attrs={'class':'form-control form-control-sm',}))
            if self.certificate_type.id==2:
                self.fields['language']=forms.ChoiceField(label='ভাষা', choices=LANGUAGE_CHOICE, widget=forms.Select( attrs={}))
            if self.certificate_type.id==3:
                self.fields['cause']=forms.ModelChoiceField(label='কারণ',queryset=Cause.objects.all(),initial=Cause.objects.filter(serial__in=[ 1,]), widget=forms.Select( attrs={'class':'form-control form-control-sm',}))
            if self.certificate_type.id==4:
                self.fields['description']=forms.CharField( label='কারণ বর্ণনা',widget=forms.Textarea( attrs={'class':'form-control form-control-sm','placeholder':'সনদেটি কি কারণে প্রয়োজন তার বর্ণনা '}))
                self.fields['language']=forms.ChoiceField(label='ভাষা', choices=LANGUAGE_CHOICE, widget=forms.Select( attrs={}))
            if self.certificate_type.id==6:
                self.fields['income']=forms.CharField( label='মাসিক আয়',widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'মাসিক আয়'}))
                self.fields['profession']=forms.CharField( label='পেশা',widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'পেশা-বৃত্তি'}))
            if self.certificate_type.id==7:
                self.fields['income']=forms.CharField( label='অভিভাবকের মাসিক আয়',widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'অভিভাবকের মাসিক আয়'}))
                self.fields['profession']=forms.CharField( label='অভিভাবকের পেশা',widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'অভিভাবকের পেশা-বৃত্তি'}))
            if self.certificate_type.id==8:
                self.fields['description']=forms.CharField( label='পরিবর্তন গুলো লিখুন',widget=forms.Textarea( attrs={'class':'form-control form-control-sm','placeholder':'সনদেটি কি কারণে প্রয়োজন তার বর্ণনা '}))
            if self.certificate_type.id==11:
                self.fields['amount']=forms.ChoiceField( choices=AMOUNT_CHOICE,label='জমির পরিমাণ(শতাংশে)',widget=forms.Select( attrs={'class':'form-control form-control-sm','placeholder':'জমির পরিমাণ উল্লেখ করুন (শতাংশে ) '}))
            if self.certificate_type.id==12:
                self.fields['dob']=forms.DateField(label='জন্ম তারিখ',widget=forms.DateInput(attrs=dict(type='date')))
                self.fields['date']=forms.DateField(label='মৃত্যু তারিখ',widget=forms.DateInput(attrs=dict(type='date')))
                self.fields['description']=forms.CharField( label='মৃত্যুর কারণ',widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'উদাহরণঃ স্বাভাবিকভাবে / দূর্ঘটনার কারণে ইত্যাদি... '}))
            if self.certificate_type.id==15:
                self.fields['date']=forms.DateField(label='স্বামীর মৃত্যু তারিখ',widget=forms.DateInput(attrs=dict(type='date')))


# class WarishanCertificateForm(forms.ModelForm):
#     class Meta:
#         model = WarishanCertificate
#         fields = "__all__"
#         exclude=['serial','name_en','email','transaction','is_verified','father_name_en','mother_name_en','tracking_no','adress','person','language']
    
            
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  '','onkeypress' : "myFunction(this.id);",'label':'Village/house'}),
#             'father_name': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  '','onkeypress' : "myFunction(this.id);",'label':'Street No.'}),
#             'mother_name': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  '','onkeypress' : "myFunction(this.id);"}),
#             'phone': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'মোবাইল নং','required':True,}),
#             'nid': forms.TextInput(attrs={'class': 'textfieldUSER', 'placeholder':  'এনআইডি অথবা জন্ম নিবন্ধন','onkeypress' : "myFunction(this.id);"}),
#             'cause': forms.Select(attrs={'class': 'textfieldUSER','onkeypress' : "myFunction(this.id);",'Hidden':True,}),
#     }
#     def __init__(self, *args, **kwargs):
#         self.certificate_type = kwargs.pop('instance', None)
#         super(WarishanCertificateForm, self).__init__(*args, **kwargs)
#         if self.certificate_type:
#             self.fields['certificate_type']=forms.ModelChoiceField(label='সনদের ধরণ',queryset=CertificateType.objects.filter(id__in=[self.certificate_type.id,]),initial=CertificateType.objects.filter(id__in=[ self.certificate_type.id,]), widget=forms.Select( attrs={'class':'textfieldUSERinfo',}))
#             # if self.certificate_type.serial==3:
#             #     self.fields['cause']=forms.ModelChoiceField(label='কারণ',queryset=Cause.objects.all(),initial=Cause.objects.filter(serial__in=[ 1,]), widget=forms.Select( attrs={'class':'textfieldUSERinfo',}))
#             # else:
#             #     self.fields['cause']=forms.ModelChoiceField(label='',queryset=Cause.objects.all(), widget=forms.Select( attrs={'class':'textfieldUSERinfo','Hidden':True,}))



class WarishForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
        exclude=['serial',]
        

class CertificateDownloadForm(forms.ModelForm):
    tracking_no= forms.CharField(label="ট্র্যাকিং নং-ঃ ",required=True, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',}))
    certificate_type= forms.ModelChoiceField(label="সার্টিফিকেটসমূহঃ ",required=True, queryset=CertificateType.objects.all().order_by('name'), widget=forms.Select(attrs={'class': 'form-control form-control-sm',}))
    class Meta:
        model = Certificate
        fields = ['tracking_no','certificate_type']
        widgets = {
            'tracking_no': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder':  'এনআইডি অথবা জন্ম নিবন্ধন','onkeypress' : "myFunction(this.id);",'required':True,}),
            'certificate_type': forms.Select(attrs={'class': 'form-control form-control-sm','onkeypress' : "myFunction(this.id);",'required':True,}),
    }



        
class AdressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = "__all__"
        exclude=['serial','holding_no','union','district','upazilla']
        widgets = {
            'village': forms.Select(attrs={'class': 'form-control form-control-sm','onchange' : "unionAdress(this.id);",'label':'Village/house','required':True}),
            'ward': forms.Select(attrs={'class': 'form-control form-control-sm', 'onchange' : "unionAdress(this.id);",'label':'Street No.','required':True}),
            'post_office': forms.Select(attrs={'class': 'form-control form-control-sm', 'onchange' : "unionAdress(this.id);" ,'required':True}),
            
}
class AdressFormExtra(forms.ModelForm):
    class Meta:
        model = Adress
        fields = "__all__"
        exclude=['serial','holding_no','union','district','upazilla']
        widgets = {
            'village': forms.Select(attrs={'class': 'form-control form-control-sm','onkeypress' : "myFunction(this.id);",'label':'Village/house','required':True}),
            'ward': forms.Select(attrs={'class': 'form-control form-control-sm','onkeypress' : "myFunction(this.id);",'label':'Street No.','required':True}),
            'post_office': forms.Select(attrs={'class': 'form-control form-control-sm', 'onkeypress' : "myFunction(this.id);",'required':True}),
            
}


