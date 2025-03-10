
import datetime
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import OthersAdress,District,Division,Union,Upazilla
from django.forms import modelformset_factory




        
class OthersAdressForm(forms.ModelForm):
    class Meta:
        model = OthersAdress
        fields = "__all__"
        exclude=['serial','holding_no',]
        widgets = {
            'village': forms.TextInput(attrs={'class': 'form-control form-control-sm','label':'Village/house','required':True}),
            'post_office': forms.TextInput(attrs={'class': 'form-control form-control-sm','required':True}),
            'union': forms.Select(choices=None,attrs={'class': 'form-control form-control-sm','onchange' : "myFunctionTeacher(this.id);",'label':'Street No.','required':True}),
            'upazilla': forms.Select(choices=None,attrs={'class': 'form-control form-control-sm','onchange' : "myFunctionTeacher(this.id);",'label':'Street No.','required':True}),
            'district': forms.Select(choices=None,attrs={'class': 'form-control form-control-sm','onchange' : "myFunctionTeacher(this.id);",'label':'Street No.','required':True}),
            'division': forms.Select(choices=Division.objects.all(),attrs={'class': 'form-control form-control-sm','onchange' : "myFunctionTeacher(this.id);",'label':'Street No.','required':True}),

}



