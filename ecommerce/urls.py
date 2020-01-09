from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import os


urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path(os.environ.get('ADMIN_URL'), admin.site.urls),

    # Allauth - auth for ecommerce
    path('accounts/', include('allauth.urls')),

    path('', include('shop.urls', namespace='ecommerce')),

    # path('rest/', include('core.urls')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

if settings.DEBUG or settings.TESTING_MODE:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
