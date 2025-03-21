from django.shortcuts import render
from django.http import JsonResponse # type: ignore
from .models import Division,District,Union,Upazilla,Ward,Village,PostOffice,Mouja
import json
# Create your views here.
def SubprocessesView(request):
        
        if request.GET.get('id')=='id_division':
            division=Division.objects.filter(id=request.GET.get('value')).first()
            district=District.objects.filter(division=division)
            district=list(district.values())
            return JsonResponse({'status': 'success','meaasge':'Account created Successfully','district':district},safe=False)
           
        if request.GET.get('id')=='id_district':
            division=District.objects.filter(id=request.GET.get('value')).first()
            district=Upazilla.objects.filter(district=division)
            district=list(district.values())
            return JsonResponse({'status': 'success','meaasge':'Account created Successfully','district':district},safe=False)
            
        if request.GET.get('id')=='id_upazilla':
            district=Upazilla.objects.filter(id=request.GET.get('value')).first()
            upazilla=Union.objects.filter(upazilla=district)
            district=list(upazilla.values())            
            return JsonResponse({'status': 'success','meaasge':'Account created Successfully','district':district},safe=False)
        return JsonResponse({'status': 'Failed','meaasge':'Account created Successfully'},safe=False)


def SubOrdinationView(request):

        if request.GET.get('id')=='id_ward':
            ward=Ward.objects.filter(id=request.GET.get('value')).first()
            print(ward)

            village=Village.objects.filter(ward=ward)
            village=list(village.values())
            return JsonResponse({'status': 'success','meaasge':'Account created Successfully','village':village},safe=False)
        if request.GET.get('id')=='id_form-0-ward':
            ward=Ward.objects.filter(id=request.GET.get('value')).first()

            village=Village.objects.filter(ward=ward)
            village=list(village.values())
            return JsonResponse({'status': 'success','meaasge':'Account created Successfully','village':village},safe=False)
        
        if request.GET.get('id')=='id_form-0-village':
            village=Village.objects.filter(id=request.GET.get('value')).first()

            mouja=Mouja.objects.filter(village=village)
            mouja=list(mouja.values())
            return JsonResponse({'status': 'success','meaasge':'Account created Successfully','mouja':mouja},safe=False)
           
                    
        return JsonResponse({'status': 'Failed','meaasge':'Account created Successfully'},safe=False)

def SubOrdinatsView(request):
     if request.GET.get('id') == 'id_form-0-division':
            division=Division.objects.filter(id=request.GET.get('value')).first()
            district=District.objects.filter(division=division)
            district=list(district.values())
            return JsonResponse({'status': 'success','meaasge':'Account created Successfully','district':district},safe=False)
     elif request.GET.get('id') == 'id_form-0-district':
            district=District.objects.filter(id=request.GET.get('value')).first()
            upazilla=Upazilla.objects.filter(district=district)
            upazilla=list(upazilla.values())
            return JsonResponse({'status': 'success','meaasge':'Account created Successfully','upazilla':upazilla},safe=False)
     elif request.GET.get('id') == 'id_form-0-upazilla':
            upazilla=Upazilla.objects.filter(id=request.GET.get('value')).first()
            union=Union.objects.filter(upazilla=upazilla)
            union=list(union.values())
            return JsonResponse({'status': 'success','meaasge':'Account created Successfully','union':union},safe=False)
        
     else:
        return JsonResponse({'status': 'Failed','meaasge':'Account created Successfully'},safe=False)
