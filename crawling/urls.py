from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', include('main_app.urls')),
                  path('settings/', include('base_settings.urls')),
                  path('admin/', admin.site.urls),
                  path('user/', include('users.urls')),
                  path('facebook/', include('facebook.urls')),
                  path('linkedin/', include('linked_in.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
