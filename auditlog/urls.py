from django.urls import path

from auditlog.views import action, get_history


urlpatterns = [
    path('auditlog/action', action),
    path('auditlog/get', get_history)
]