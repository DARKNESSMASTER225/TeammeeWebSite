from django.urls import path, include
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('users/', include('users.urls')),
    path('tarifs', views.tariffs, name='tariffs'),
    path('tariff/checkout/', views.checkout),
    path('', views.main, name='main'),
]
