"""
Main URL Configuration for PenTutor Backend
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# API URL patterns
api_v1_patterns = [
    # Authentication URLs
    path('auth/', include('services.authentication.urls')),
    
    # JWT Token URLs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # # Service URLs
    # path('meetings/', include('services.meetings.urls')),
    # path('lms/', include('services.lms.urls')),
    # path('ai/', include('services.ai_services.urls')),
    # path('payments/', include('services.payments.urls')),
    # path('jobs/', include('services.job_board.urls')),
    # path('notifications/', include('services.notifications.urls')),
]

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # API v1
    path('api/v1/', include(api_v1_patterns)),
    
    # Django Allauth
    path('accounts/', include('allauth.urls')),
    
    # Health check endpoint
    path('health/', lambda request: HttpResponse('OK')),
]

# Static and Media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    # Django Debug Toolbar
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns

# Add HttpResponse import
from django.http import HttpResponse