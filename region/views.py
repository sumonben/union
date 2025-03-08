from django.shortcuts import render
from django.http import JsonResponse # type: ignore
from .models import Division,District,Union,Upazilla
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
