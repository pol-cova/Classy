from django.urls import path, include
from .views import index, home, user_login

urlpatterns = [
    path('', index , name='index'),
    path('my/', home, name='home'),
    # test login route
    path('login/', user_login, name='login')
]