from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework import generics
from django.http import HttpResponse
from .models import UserModel
from .serializers import UserSerializer

class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer

class UserList(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer