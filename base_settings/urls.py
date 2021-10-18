from django.urls import path
from base_settings.views import *

app_name = 'base_settings'

urlpatterns = [
    path('apps-name', get_all_application_name, name='apps_name_url'),
    path('app/apis-name', get_all_application_api_name, name='app_apis_name'),
    path('app/api/input-fields-name', get_all_application_api_input_field_name, name='app_api_input_fields_name'),
]
