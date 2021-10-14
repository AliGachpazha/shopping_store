from django.contrib.auth.hashers import check_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from rest_framework import generics, permissions, status, authentication, viewsets, generics, mixins
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, ChangeCustomerPasswordSerializer
from rest_framework.response import Response
from rest_framework.utils import json
from customer.models import User
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.decorators import action
from rest_framework.response import Response


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, many=False).data,
            "token": AuthToken.objects.create(user)[1]
        })


class ChangeCustomerPassword(APIView, mixins.UpdateModelMixin):
    # taking token and checking valuable
    query_set = {}
    # permission_classes = [IsAuthenticated]
    serializer_class = ChangeCustomerPasswordSerializer

    def post(self, request, *args, **kwargs):

        serialized_customer = ChangeCustomerPasswordSerializer(data=request.data)
        if serialized_customer.is_valid(raise_exception=True):
            try:
                token = serialized_customer.data['token']
                user = Token.objects.get(key=token).user
            except Token.DoesNotExist:
                return Response({'msg': 'user does not exist'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            passwords = serialized_customer.data
            if passwords['password1'] != passwords['password2'] or not check_password(passwords['password'],
                                                                                      user.password):
                return Response({'msg': 'password does not match'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            user.set_password(passwords['password2'])
            user.save()
            return Response({'msg': 'password changed successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response({'msg': 'invalid data'}, status=status.HTTP_400_BAD_REQUEST)
