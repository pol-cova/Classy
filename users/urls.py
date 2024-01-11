from django.urls import path, include
from .views import index, home, user_login, user_signup, user_logout, user_profile,complete_profile, edit_profile, delete_account

urlpatterns = [
    path('', index , name='index'),
    path('my/', home, name='home'),
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='profile'),
    path('profile/complete/', complete_profile, name='complete_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/delete/', delete_account, name='delete_account'),
]