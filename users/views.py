from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions

from rest_framework.generics import GenericAPIView, ListAPIView

from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

import users.models
from Apartment.serializers import MyPagination
from users import serializers
from .send_mail import send_confirmation_email

from django.contrib.auth import get_user_model

from rest_framework import status, generics
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.response import Response
import logging
# from .serializers import LogoutSerializer

# from .serializers import LogoutSerializer

from django.views.decorators.cache import cache_page
from .serializers import RefreshTokenSerializer

from rest_framework.filters import SearchFilter

User = get_user_model()

class RegistrationView(APIView):
    pagination_class = MyPagination

    permission_classes = (permissions.AllowAny,)

    @cache_page(60 * 5)  # кэш на 5 минут
    def post(self, request):
        serializer = serializers.RegistrationSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print("USER ACT VALID=>", user.activation_code)
        if user:
            try:
                send_confirmation_email(user.email, user.activation_code)
            except User.DoesNotExist:
                return Response({'msg': 'Registered, but troubles with email!', 'data': serializer.data}, status=201)
        return Response(serializer.data, status=201)

class ActivationView(GenericAPIView):
    pagination_class = MyPagination

    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.ActivationSerializer

    @cache_page(60 * 5)  # кэш на 5 минут
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Successfully activated!', status=200)


class LoginView(TokenObtainPairView):
    pagination_class = MyPagination

    permission_classes = (permissions.AllowAny,)


class UserListApiView(ListAPIView):
    pagination_class = MyPagination


    queryset = User.objects.all().order_by('id')
    serializer_class = serializers.UserSerializer

    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['username', 'email']
    filterset_fields = {
        'username': ['exact'],  # фильтр для user__username
    }



class LogoutView(generics.GenericAPIView):

    pagination_class = MyPagination

    serializer_class = RefreshTokenSerializer
    # permission_classes = (permissions.IsAuthenticated, )

    @cache_page(60 * 5)  # кэш на 5 минут
    def post(self, request, *args):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data.get('user')
            serializer.save()
            return Response({"Сообщение": "Вы успешно вышли из системы.", "Пользователь": user.username}, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


logger = logging.getLogger(__name__)


class MyView(APIView):

    pagination_class = MyPagination

    @cache_page(60 * 5)  # кэш на 5 минут
    def get(self, request):
        logger.debug('Debug message')
        logger.info('Info message')
        logger.warning('Warning message')
        logger.error('Error message')
        logger.critical('Critical message')
        return Response({'message': 'Hello, world!'})