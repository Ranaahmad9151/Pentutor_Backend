from django.urls import path
from .viewsets.auth import (
    register,
    login,
    logout,
    verify_email,
    resend_verification,
    change_password,
    password_reset_request,
    password_reset_confirm,
    google_auth,
    apple_auth
)
from .viewsets.user import profile, update_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/update/', update_profile, name='update_profile'),
    path('verify-email/', verify_email, name='verify_email'),
    path('resend-verification/', resend_verification, name='resend_verification'),
    path('change-password/', change_password, name='change_password'),
    path('password-reset/', password_reset_request, name='password_reset_request'),
    path('password-reset/confirm/', password_reset_confirm, name='password_reset_confirm'),
    path('google-auth/', google_auth, name='google_auth'),
    path('apple-auth/', apple_auth, name='apple_auth'),
]