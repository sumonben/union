from django.contrib import admin
from django.urls import path,include, re_path
import static
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django import views as django_views
from django.views.decorators.cache import cache_page


urlpatterns = [
    
    path('',(views.HomeView.as_view()), name='home'),
    path('apply_for_certificate/<int:id>/',views.ApplyForCertificate.as_view(), name='apply_for_certificate'),
    path('select_certificate/',views.SelectCertificate.as_view(), name='select_certificate'),
    path('certificate_form/', views.CertificateView.as_view(), name="certificate_form"),
    path('submit_form/', views.submitFormView.as_view(), name="submit_form"),
    path('download_certificate_form/', views.DownloadCertificateView.as_view(), name="download_certificate_form"),
    path('download_applicants_copy_form/', views.DownloadApplicantsCopyView.as_view(), name="download_applicants_copy_form"),
    path('check_certificate_form/', views.DownloadCertificateView.as_view(), name="check_certificate_form"),
    path('front/', views.FrontView.as_view(), name="front"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('tutorial/', views.TutorialView.as_view(), name="tutorial"),





]

'''path('admission_form/', views.admissionForm, name="admission_form"),
    path('admission_form_submit/', views.admissionFormSubmit, name="admission_form_submit"),
    path('form-download/', views.formDownload, name='form-download'),

    path('jsi18n/', django_views.i18n.JavaScriptCatalog.as_view(), name='jsi18n'),'''

