from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import StorageListView, register_group_user, get_info, get_group_members, edit_access_layer, delete_user

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/storages/', StorageListView.as_view(), name='storage-list'),
    path('api/createuser/', register_group_user),
    path('api/infome/', get_info),
    path('api/infogroup/', get_group_members),
    path('api/edit_access_layer/', edit_access_layer),
    path('api/member/', delete_user)

]

