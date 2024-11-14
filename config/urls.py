from django.contrib import admin
from django.urls import path, include
from app.views import my_view
from django.conf.urls.static import static
from config import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', my_view, name='index'),
]+ i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('app.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
