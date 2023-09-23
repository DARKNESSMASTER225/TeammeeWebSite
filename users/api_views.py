from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.middleware import csrf
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import Profile
from django.core.exceptions import ValidationError
class CustomTokenObtainPairView(TokenObtainPairView):
    pass
def is_valid_username(username):
    try:

        User.objects.get(username=username)
        return True
    except User.DoesNotExist:
        return False

class CustomAuthToken(APIView):
    def post(self, request, *args, **kwargs):

        username = request.data.get('username')
        if not ( is_valid_username(username)) :
            return Response("Некорректные данные" , status=status.HTTP_200_OK)
        password = request.data.get('password')
        csrf_token = request.META.get("HTTP_X_CSRFTOKEN")
        if not csrf_token:
            return Response({"detail": "CSRF token missing."}, status=status.HTTP_401_UNAUTHORIZED)


        if not username or not password:
            return Response({'detail': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)

        if not (user.check_password(password) ) :
            return Response("Некорректные данные" , status=status.HTTP_200_OK)


        info_data = {
            "username": user.username,
            "tarif_level": profile.tarif_level,
            "access_level": profile.access_level,
            "id": user.id,
            "email": user.email,
        }


        return Response(info_data, status=status.HTTP_200_OK)

class GetCSRFToken(APIView):
    def get(self, request):
        csrf_token = csrf.get_token(request)
        return Response({'csrf_token': csrf_token})
