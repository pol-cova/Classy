from django.urls import path, include
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from .views import index, home,login_page, user_login,signup_page, user_signup, user_logout, user_profile,complete_profile, edit_profile, delete_account

urlpatterns = [
    path('', index , name='index'),
    path('my/', home, name='home'),
    path('login/', login_page, name='login_page'),
    path('auth/login/', user_login, name='login'),
    path('signup/', signup_page, name='signup_page'),
    path('auth/signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='profile'),
    path('profile/complete/', complete_profile, name='complete_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/delete/', delete_account, name='delete_account'),
    
    # Passwords systems urls
    path('password_reset/', PasswordResetView.as_view(template_name = 'password_reset.html',
                                            html_email_template_name ='password_reset_email.html'), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'), name='password_reset_complete'),
    
]