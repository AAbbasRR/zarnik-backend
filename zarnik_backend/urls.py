from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Login.urls', namespace='login')),
    path('dashboard/', include('Dashboard.urls', namespace='dashboard')),
    path('product/', include('Product.urls', namespace='product')),
    path('section/', include('Section.urls', namespace='section')),
    path('setting/', include('Setting.urls', namespace='setting')),
    path('newsletters/', include('Newsletters.urls', namespace='newsletters')),
    path('api/', include('api.urls', namespace='api')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()