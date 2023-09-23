# userauth/urls.py

from django.urls import path
from . import views
from .api_views import CustomAuthToken, GetCSRFToken


urlpatterns = [
    path('register/', user_views.register, name='register'),
path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),
path('users/', include('users.urls')),
path('tarifs', user_views.tarifs, name='tarifs'),
path('accounts/profile/', views.profile_view, name='profile'),

path('api/auth_token/', CustomAuthToken.as_view(), name='user-profile'),
path('api/get_csrf_token/', GetCSRFToken.as_view(), name='get-csrf-token'),

path('', user_views.main, name='maim'),
]
