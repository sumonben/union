from django.contrib import admin
from django.urls import path,include, re_path
import static
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django import views as django_views


urlpatterns = [
    
    path('apply_for_license/<int:id>/',views.ApplyForLicense.as_view(), name='apply_for_license'),
    # path('select_license/',views.SelectLicense.as_view(), name='select_license'),
    path('license_form/', views.LicenseView.as_view(), name="license_form"),
    path('submit__license_form/', views.submitLicenseFormView.as_view(), name="submit__license_form"),
    path('download_license_form/', views.DownloadLicenseView.as_view(), name="download_license_form"),
    path('check_license_form/', views.DownloadLicenseView.as_view(), name="check_license_form"),
   





]

'''path('admission_form/', views.admissionForm, name="admission_form"),
    path('admission_form_submit/', views.admissionFormSubmit, name="admission_form_submit"),
    path('form-download/', views.formDownload, name='form-download'),

    path('jsi18n/', django_views.i18n.JavaScriptCatalog.as_view(), name='jsi18n'),'''

