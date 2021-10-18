from django.urls import path, include

app_name = 'facebook_crawler'
urlpatterns = [

    path('api/', include('facebook.api.urls')),
]
