from django.urls import path, include
from .views import index, home, user_login, user_signup, user_logout

urlpatterns = [
    path('', index , name='index'),
    path('my/', home, name='home'),
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout')
]