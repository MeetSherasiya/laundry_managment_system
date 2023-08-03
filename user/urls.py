from django.urls import path
from .views import *
from user.views import CustomPasswordResetView
from django.urls import path
from django.contrib.auth.views import (
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('', index, name="index"),
    path('login/', userlogin, name="login"),
    path('change-password/', change_password, name="change_password"),
    path('profile/', user_profile, name="user_profile"),
    path('register/', userregister, name="register"),
    path('verify/<token>/', verify, name="verify"),
    path('newreq/', new_request, name="new_request"),

    path('password-reset/', CustomPasswordResetView.as_view() ,name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
]
