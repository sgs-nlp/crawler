from django.urls import path, include

urlpatterns = [
    path('crawling/linkedin/', include('linked_in.urls')),
]
