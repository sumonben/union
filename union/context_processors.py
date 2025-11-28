from django.conf import settings
from .models import UnionDetails, ColorRoot
from certificate.models import CertificateType
from license.models import LicenseType
def site_info(request):
        union_details=UnionDetails.objects.filter(is_active=True).last()
        certificate_types=CertificateType.objects.all().order_by('serial')
        license_types=LicenseType.objects.all().order_by('serial')
        color=ColorRoot.objects.filter(is_active=True).first()
        if union_details:
            return {
                'SITE_NAME': union_details.name,
                'POST_OFFICE': union_details.post_office.name if union_details.post_office else None,
                'UPAZILLA':union_details.upazilla.name,
                'DISTRICT':union_details.district.name,
                'LOGO': union_details.logo.url,
                'certificate_types': certificate_types,
                'license_types': license_types,
                'union_details': union_details,
                'color':color,
            }
        return {}

