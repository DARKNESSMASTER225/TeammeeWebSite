from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from users.api_views import CustomAuthToken, GetCSRFToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
path('', user_views.main, name='main'),
    path('accounts/profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
path('tarifs', user_views.tarifs, name='tarifs'),

path('api/get_csrf_token/', GetCSRFToken.as_view(), name='get-csrf-token'),
path('api/auth_token/', CustomAuthToken.as_view(), name='user-profile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)