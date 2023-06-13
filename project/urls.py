from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

urlpatterns = [
    path('accounts/', include('accounts.urls' , namespace='accounts')),
    path('', include('jop.urls' , namespace='jops')),
    path('contact-us/', include('contact.urls' , namespace='contact')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
handler404 = 'jop.views.error_404'

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
