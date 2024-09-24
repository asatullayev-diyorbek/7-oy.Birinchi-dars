from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path('auth/', include('register.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
