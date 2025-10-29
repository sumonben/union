from django.conf import settings
from .models import UnionDetails
def site_info(request):
        union_details=UnionDetails.objects.last()
        return {
            'SITE_NAME': union_details.name,
            'POST_OFFICE': union_details.post_office.name,
            'UPAZILLA':union_details.upazilla.name,
            'DISTRICT':union_details.district.name,
            'LOGO': union_details.logo.url,
        }
