
import datetime
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import HoldingTax, HoldingType, FiscalYear
from region.models import Ward, Village,PostOffice
from django.forms import modelformset_factory
from django.contrib.admin.widgets import AdminDateWidget
from region.models import OthersAdress,Division
from ckeditor.widgets import CKEditorWidget


class HoldingTaxSearchForm(forms.ModelForm):
    
    class Meta:
        model = HoldingTax
        fields = "__all__"
        exclude=['serial','name_en','name','phone','email','transaction','is_paid','father_name_en','mother_name_en','father_name','mother_name','nid','amount']
    
    def __init__(self, *args, **kwargs):
        super(HoldingTaxSearchForm, self).__init__(*args, **kwargs)
        self.fields['holding_no']=forms.CharField(label='হোল্ডিং নাম্বার', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'হোল্ডিং নাম্বার লিখুন ইংরেজিতে'}))
        self.fields['fiscal_year']=forms.ModelChoiceField(label='অর্থ-বছর',queryset=FiscalYear.objects.all(), widget=forms.Select( attrs={'class':'form-control form-control-sm',}))
        self.fields['holding_type']=forms.ModelChoiceField(label='হোল্ডিং ট্যাক্সের ধরণ',queryset=HoldingType.objects.all(), widget=forms.Select( attrs={'class':'form-control form-control-sm','onchange':'MaritalStatusChanged(this.id)'}))

class HoldingTaxForm(forms.ModelForm):
    
    class Meta:
        model = HoldingTax
        fields = "__all__"
        exclude=['serial','name_en','transaction','is_paid','father_name_en','mother_name_en',]
    
            
        
    def __init__(self, *args, **kwargs):
        self.holding_tax = kwargs.pop('instance', None)
        # holding_tax=HoldingTax.objects.filter(id=self.holding_no.id).first()
        super(HoldingTaxForm, self).__init__(*args, **kwargs)
        if self.holding_tax.holding_no:
            self.fields['holding_no']=forms.CharField(label='হোল্ডিং নাম্বার', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','value':self.holding_tax.holding_no,'readonly':True}))
        else:
            self.fields['holding_no']=forms.CharField(label='হোল্ডিং নাম্বার', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'হোল্ডিং নাম্বার লিখুন ইংরেজিতে'}))
        if self.holding_tax.fiscal_year:
            self.fields['fiscal_year']=forms.ModelChoiceField(label='অর্থ-বছর',queryset=FiscalYear.objects.filter(id=self.holding_tax.fiscal_year.id),initial=self.holding_tax.fiscal_year, widget=forms.Select( attrs={'class':'form-control form-control-sm',}))
        else:
            self.fields['fiscal_year']=forms.ModelChoiceField(label='অর্থ-বছর',queryset=FiscalYear.objects.all(), widget=forms.Select( attrs={'class':'form-control form-control-sm',}))
        if self.holding_tax.holding_type:
            self.fields['holding_type']=forms.ModelChoiceField(label='হোল্ডিং ট্যাক্সের ধরণ',queryset=HoldingType.objects.filter(id=self.holding_tax.holding_type.id),initial=self.holding_tax.holding_type, widget=forms.Select( attrs={'class':'form-control form-control-sm','onchange':'MaritalStatusChanged(this.id)'}))
        else:
            self.fields['holding_type']=forms.ModelChoiceField(label='হোল্ডিং ট্যাক্সের ধরণ',queryset=HoldingType.objects.all(), widget=forms.Select( attrs={'class':'form-control form-control-sm','onchange':'MaritalStatusChanged(this.id)'}))
        if self.holding_tax.amount:
            self.fields['amount']=forms.CharField(label='পরিমান(টাকা)', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','value':self.holding_tax.amount,'readonly':True}))
        else:
            self.fields['amount']=forms.CharField(label='পরিমান(টাকা)', widget=forms.TextInput( attrs={'class':'form-control form-control-sm',}))
        if self.holding_tax.name:
            self.fields['name']=forms.CharField(label='প্রদানকারীর নাম', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','value':self.holding_tax.name,'readonly':True}))
        else:
            self.fields['name']=forms.CharField(label='প্রদানকারীর নাম', widget=forms.TextInput( attrs={'class':'form-control form-control-sm',}))
        if self.holding_tax.phone:
            self.fields['phone']=forms.CharField(label='মোবাইল', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','value':self.holding_tax.phone,'readonly':True}))
        else:
            self.fields['phone']=forms.CharField(label='মোবাইল', widget=forms.TextInput( attrs={'class':'form-control form-control-sm',}))
        if self.holding_tax.email:
            self.fields['email']=forms.CharField(label='ই-মেইল', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','value':self.holding_tax.email,'readonly':True}))
        else:
            self.fields['email']=forms.CharField(label='ই-মেইল', widget=forms.TextInput( attrs={'class':'form-control form-control-sm',}))
        if self.holding_tax.nid:
            self.fields['nid']=forms.CharField(label='জাতীয় পরিচয়/জন্ম নিবন্ধন', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','value':self.holding_tax.nid,'readonly':True}))
        else:
            self.fields['nid']=forms.CharField(label='জাতীয় পরিচয়/জন্ম নিবন্ধন', widget=forms.TextInput( attrs={'class':'form-control form-control-sm',}))
        if self.holding_tax.father_name:
            self.fields['father_name']=forms.CharField(label='বাবার নাম', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','value':self.holding_tax.father_name,'readonly':True}))
        else:
            self.fields['father_name']=forms.CharField(label='বাবার নাম', widget=forms.TextInput( attrs={'class':'form-control form-control-sm',}))
        if self.holding_tax.mother_name:
            self.fields['mother_name']=forms.CharField(label='মায়ের নাম', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','value':self.holding_tax.mother_name,'readonly':True}))
        else:
            self.fields['mother_name']=forms.CharField(label='মায়ের নাম', widget=forms.TextInput( attrs={'class':'form-control form-control-sm',}))
        
        if self.holding_tax.village:
            self.fields['village']=forms.ModelChoiceField(label='গ্রাম/মহল্লা',queryset=Village.objects.filter(id=self.holding_tax.village.id),initial=self.holding_tax.village, widget=forms.Select( attrs={'class':'form-control form-control-sm','onchange':'MaritalStatusChanged(this.id)'}))
        else:
            self.fields['village']=forms.ModelChoiceField(label='গ্রাম/মহল্লা',queryset=Village.objects.all(), widget=forms.Select( attrs={'class':'form-control form-control-sm','onchange':'MaritalStatusChanged(this.id)'}))
        if self.holding_tax.ward:
            self.fields['ward']=forms.ModelChoiceField(label='ওয়ার্ড',queryset=Ward.objects.filter(id=self.holding_tax.ward.id),initial=self.holding_tax.ward, widget=forms.Select( attrs={'class':'form-control form-control-sm','onchange':'MaritalStatusChanged(this.id)'}))
        else:
            self.fields['ward']=forms.ModelChoiceField(label='ওয়ার্ড',queryset=Ward.objects.all(), widget=forms.Select( attrs={'class':'form-control form-control-sm','onchange':'MaritalStatusChanged(this.id)'}))

        # self.fields['village']=forms.CharField(label='মায়ের নাম', widget=forms.TextInput( attrs={'class':'form-control form-control-sm',}))
        # self.fields['ward']=forms.CharField(label='মায়ের নাম', widget=forms.TextInput( attrs={'class':'form-control form-control-sm',}))
        # # self.fields['post_office']=forms.CharField(label='মায়ের নাম', widget=forms.TextInput( attrs={'class':'form-control form-control-sm',}))
        # self.fields['fiscal_year']=forms.ModelChoiceField(label='অর্থ-বছর',queryset=FiscalYear.objects.all(), widget=forms.Select( attrs={'class':'form-control form-control-sm',}))
        # self.fields['holding_type']=forms.ModelChoiceField(label='হোল্ডিং ট্যাক্সের ধরণ',queryset=HoldingType.objects.all(), widget=forms.Select( attrs={'class':'form-control form-control-sm','onchange':'MaritalStatusChanged(this.id)'}))
        # self.fields['gender']=forms.ModelChoiceField(label='লিঙ্গ',queryset=Gender.objects.all(), widget=forms.Select( attrs={'class':'form-control form-control-sm','onchange':'GenderChanged(this.id)'}))
        
        
    #     if self.certificate_type:
    #         self.fields['certificate_type']=forms.ModelChoiceField(label='সনদের ধরণ',queryset=CertificateType.objects.filter(id__in=[self.certificate_type.id,]),initial=CertificateType.objects.filter(id__in=[ self.certificate_type.id,]), widget=forms.Select( attrs={'class':'form-control form-control-sm',}))
    #         if self.certificate_type.id==2 or self.certificate_type.id == 4 or self.certificate_type.id==24 or self.certificate_type.id==27 or self.certificate_type.id == 28 or self.certificate_type.id == 29:
    #             self.fields['language']=forms.ChoiceField(label='ভাষা', choices=LANGUAGE_CHOICE, widget=forms.Select( attrs={}))
    #         if self.certificate_type.id==3:
    #             self.fields['cause']=forms.ModelChoiceField(label='কারণ',queryset=Cause.objects.all(),initial=Cause.objects.filter(serial__in=[ 1,]), widget=forms.Select( attrs={'class':'form-control form-control-sm',}))
    #         if self.certificate_type.id==4:
    #             self.fields['description']=forms.CharField( label='প্রত্যয়নের বিষয় (সুপারিশসহ)',widget=CKEditorWidget(config_name='default'))
    #             # self.fields['language']=forms.ChoiceField(label='ভাষা', choices=LANGUAGE_CHOICE, widget=forms.Select( attrs={}))
    #         if self.certificate_type.id==6:
    #             self.fields['income']=forms.CharField( label='মাসিক আয়',widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'১০****/= (একহাজার টাকা) এভাবে লিখতে হবে'}))
    #             self.fields['profession']=forms.CharField( label='পেশা',widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'পেশা-বৃত্তি'}))
    #         if self.certificate_type.id==7:
    #             self.fields['income']=forms.CharField( label='অভিভাবকের মাসিক আয়',widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'১০****/= (একহাজার টাকা) এভাবে লিখতে হবে'}))
    #             self.fields['profession']=forms.CharField( label='অভিভাবকের পেশা',widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'অভিভাবকের পেশা-বৃত্তি'}))
    #         if self.certificate_type.id==8 or self.certificate_type.id==21 :
    #             self.fields['description']=forms.CharField( label='সংশোধন এর পরিবর্তন গুলো লিখুন',widget=CKEditorWidget(config_name='default'))
    #         if self.certificate_type.id==11:
    #             self.fields['amount']=forms.ChoiceField( choices=AMOUNT_CHOICE,label='জমির পরিমাণ(শতাংশে)',widget=forms.Select( attrs={'class':'form-control form-control-sm','placeholder':'জমির পরিমাণ উল্লেখ করুন (শতাংশে ) '}))
    #         if self.certificate_type.id==12:
    #             self.fields['language']=forms.ChoiceField(label='ভাষা', choices=LANGUAGE_CHOICE, widget=forms.Select( attrs={}))
    #             self.fields['dob']=forms.DateField(label='জন্ম তারিখ',widget=forms.DateInput(attrs=dict(type='date')))
    #             self.fields['date']=forms.DateField(label='মৃত্যু তারিখ',widget=forms.DateInput(attrs=dict(type='date')))
    #             self.fields['description']=forms.CharField( label='মৃত্যুর কারণ',widget=CKEditorWidget(config_name='default'))
    #             self.fields['passport']=forms.CharField( label='পাসপোর্ট নং (যদি থাকে)',widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'প্রযোজ্য ক্ষেত্রে(বিদেশ বিষয়ে কোন সংশ্লিষ্টতা থাকলে)'}))
    #         if self.certificate_type.id== 15:
    #             self.fields['date']=forms.DateField(label='স্বামীর মৃত্যু তারিখ',widget=forms.DateInput(attrs=dict(type='date')))
    #         if self.certificate_type.id== 16:
    #             self.fields['title']=forms.CharField(required=False,label='সনদের শিরোনামঃ', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'সনদের শিরোনামে যা দেখতে চান'}))
    #             self.fields['language']=forms.ChoiceField(label='ভাষা', choices=LANGUAGE_CHOICE, widget=forms.Select( attrs={}))
    #             self.fields['description']=forms.CharField( label='সনদের বডি অংশ',widget=CKEditorWidget(config_name='default'))
    #         if self.certificate_type.id==17:
    #             self.fields['language']=forms.ChoiceField(label='আদিবাসীর ভাষা', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'আদিবাসীর ভাষা'}))
    #             self.fields['caste']=forms.ChoiceField(label='আদিবাসীর গোত্রের নাম', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'গোত্রের নাম লিখুন'}))
    #         if self.certificate_type.id==19:
    #             self.fields['title']=forms.ChoiceField(label='যে মৃত(বাছাই করুন)',choices=ORPHAN_CHOICE, widget=forms.Select( attrs={'class':'form-control form-control-sm','placeholder':'বিদেশ গেলে দেশের নাম বা যা করতে ছারপ্ত্র তা লিখুন','required':'required'}))
    #         if self.certificate_type.id==20:
    #             self.fields['title']=forms.ChoiceField(label='সেক্টর নং', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'বাংলায় লিখুন, যেমন- ০১/০২/০৩ ','required':'required'}))

    #         if self.certificate_type.id==22:
    #             self.fields['title']=forms.CharField(label='যেখানে যেতে বা যা করতে', widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'বিদেশ গেলে দেশের নাম বা যা করতে ছারপ্ত্র তা লিখুন'}))
    #             self.fields['language']=forms.ChoiceField(label='ভাষা', choices=LANGUAGE_CHOICE, widget=forms.Select( attrs={}))

    #         if self.certificate_type.id== 23:
    #             self.fields['title']=forms.CharField( label='বর্তমান ভোটার ঠিকানা',widget=forms.TextInput( attrs={'class':'form-control form-control-sm','placeholder':'এভাবে লিখুনঃ গ্রাম/মহল্লাঃ ***, ডাকঘরঃ ***, উপজেলাঃ**, জেলাঃ ***'}))
    #             self.fields['cause']=forms.ModelChoiceField(label='কারণ',queryset=Cause.objects.all(),initial=Cause.objects.filter(serial__in=[ 1,]), widget=forms.Select( attrs={'class':'form-control form-control-sm',}))
    #         if self.certificate_type.id==25 :
    #             self.fields['date']=forms.DateField(label='স্বামী/স্ত্রীর মৃত্যু তারিখ',widget=forms.DateInput(attrs=dict(type='date')))


