from django.contrib import admin
from django.urls import path,include, re_path # type: ignore
import static
from . import views


urlpatterns = [
    
    path('', views.SubprocessesView, name='get_district'),
    path('subordinations/', views.SubOrdinationView, name='get_subordinations'),

    # path('jsi18n/', django_views.i18n.JavaScriptCatalog.as_view(), name='jsi18n'),

]