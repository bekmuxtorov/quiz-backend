from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from quiz.views import index_view


urlpatterns = [
    path('', index_view, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('accounts/', include('accounts.urls')),
    path('quiz/', include('quiz.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
