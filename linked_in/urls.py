from django.urls import path, include


app_name = 'linkedin_crawler'
urlpatterns = [
    path('api/', include('linked_in.api.urls')),
]
