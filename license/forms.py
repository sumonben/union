
import datetime
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Adress,Person,LicenseType,License
from region.models import Ward,Village,PostOffice,Mouja
from django.forms import modelformset_factory
from certificate.forms import LANGUAGE_CHOICE

AdressFormSet = modelformset_factory(
    Adress, fields=('mouja','village','ward','post_office'), extra=1,
    widgets = {
            'mouja': forms.Select(choices=Mouja.objects.all(),attrs={'class': 'form-control form-control-sm' , 'onchange' : "unionAdress(this.id);"}),
            'village': forms.Select(choices=Village.objects.all(),attrs={'class': 'form-control form-control-sm', 'onchange' : "unionAdress(this.id);",}),
            'ward': forms.Select(choices=Ward.objects.all(),attrs={'class': 'form-control form-control-sm', 'onchange' : "unionAdress(this.id);"}),            
            'post_office': forms.Select(choices=PostOffice.objects.all(),attrs={'class': 'form-control form-control-sm',}),            
        }
)

class LicenseTypeForm(forms.ModelForm):
    name= forms.ModelChoiceField(label="সার্টিফিকেটসমূহঃ ",required=True,queryset=LicenseType.objects.all(),widget=forms.Select(attrs={'class': 'form-control form-control-sm',}))
    class Meta:
        model = LicenseType
        fields = []

class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = "__all__"
        exclude=['serial','licensed_name_en','transaction','is_verified','father_name_en','mother_name_en','passport','tax','fee','vat_n_others','license_no','memorial_no','tracking_no','adress','description','cause','person','chairman','member','caste','income','profession','language']
    
            
        
    def __init__(self, *args, **kwargs):
        self.license_type = kwargs.pop('instance', None)
        super(LicenseForm, self).__init__(*args, **kwargs)
        self.fields['licensed_name']=forms.CharField(label='নাম', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'নাম লিখুন'}))
        self.fields['license_owner_name']=forms.CharField(label='নাম', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'নাম লিখুন'}))
        self.fields['phone']=forms.CharField(label='মোবাইল', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'ie: 01*********'}))
        self.fields['email']=forms.CharField(label='ই-মেইল', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'ie: *****@***.com'}))
        self.fields['nid']=forms.CharField(required=True,label='জাতীয় পরিচয়/জন্ম নিবন্ধন', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'না থাকলে প্রয়োজন নেই'}))
        self.fields['father_name']=forms.CharField(label='বাবার নাম', widget=forms.TextInput( attrs={'class':'form-control form-control-sm',}))
        self.fields['mother_name']=forms.CharField(label='মায়ের নাম', widget=forms.TextInput( attrs={'class':'form-control form-control-sm',}))

        if self.license_type:
            self.fields['license_type']=forms.ModelChoiceField(label='লাইসেন্সের ধরণ',queryset=LicenseType.objects.filter(id__in=[self.license_type.id,]),initial=LicenseType.objects.filter(id__in=[ self.license_type.id,]), widget=forms.Select( attrs={'class':'form-control form-control-sm',}))
            if self.license_type.id==2:
                self.fields['language']=forms.ChoiceField(label='ভাষা', choices=LANGUAGE_CHOICE, widget=forms.Select( attrs={}))
            if self.license_type.id==4:
                self.fields['description']=forms.CharField( label='কারণ বর্ণনা',widget=forms.Textarea( attrs={'class':'form-control form-control-sm','placeholder':'সনদেটি কি কারণে প্রয়োজন তার বর্ণনা '}))
                self.fields['language']=forms.ChoiceField(label='ভাষা', choices=LANGUAGE_CHOICE, widget=forms.Select( attrs={}))
            if self.license_type.id==6:
                self.fields['income']=forms.CharField( label='মাসিক আয়',widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'মাসিক আয়'}))
                self.fields['profession']=forms.CharField( label='পেশা',widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'পেশা-বৃত্তি'}))
            if self.license_type.id==7:
                self.fields['income']=forms.CharField( label='অভিভাবকের মাসিক আয়',widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'অভিভাবকের মাসিক আয়'}))
                self.fields['profession']=forms.CharField( label='অভিভাবকের পেশা',widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'অভিভাবকের পেশা-বৃত্তি'}))
            if self.license_type.id==8:
                self.fields['description']=forms.CharField( label='পরিবর্তন গুলো লিখুন',widget=forms.Textarea( attrs={'class':'form-control form-control-sm','placeholder':'সনদেটি কি কারণে প্রয়োজন তার বর্ণনা '}))
       
class LicenceDownloadForm(forms.ModelForm):
    tracking_no= forms.CharField(label="ট্র্যাকিং নং-ঃ ",required=True, widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',}))
    license_type= forms.ModelChoiceField(label="লাইসেন্সসমূহঃ ",required=True, queryset=LicenseType.objects.all(), widget=forms.Select(attrs={'class': 'form-control form-control-sm',}))
    class Meta:
        model = License
        fields = ['tracking_no','license_type']
        widgets = {
            'tracking_no': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder':  'এনআইডি অথবা জন্ম নিবন্ধন','onkeypress' : "myFunction(this.id);",'required':True,}),
            'license_type': forms.Select(attrs={'class': 'form-control form-control-sm','onkeypress' : "myFunction(this.id);",'required':True,}),
    }
