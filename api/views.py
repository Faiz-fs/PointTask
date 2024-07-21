from django.shortcuts import render, redirect
from rest_framework import generics
from .models import User, AppDetails, TaskDetail
from .serializer import UserSerializer, AppDetailsSerializer, TaskDetailSerializer

# Create your views here.


# View to list and create users
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()  # Query to retrieve all users
    serializer_class = UserSerializer  # Serializer to use for the User model


# View to retrieve, update, and delete a specific user
class UserRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()  # Query to retrieve all users
    serializer_class = UserSerializer  # Serializer to use for the User model


# View to list and create app details
class AppDetailsListCreate(generics.ListCreateAPIView):
    queryset = AppDetails.objects.all()  # Query to retrieve all app details
    serializer_class = (
        AppDetailsSerializer  # Serializer to use for the AppDetails model
    )


# View to retrieve, update, and delete a specific app detail
class AppDetailsRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppDetails.objects.all()  # Query to retrieve all app details
    serializer_class = (
        AppDetailsSerializer  # Serializer to use for the AppDetails model
    )


# View to list and create task details
class TaskDetailListCreate(generics.ListCreateAPIView):
    queryset = TaskDetail.objects.all()  # Query to retrieve all task details
    serializer_class = (
        TaskDetailSerializer  # Serializer to use for the TaskDetail model
    )


# View to retrieve, update, and delete a specific task detail
class TaskDetailRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskDetail.objects.all()  # Query to retrieve all task details
    serializer_class = (
        TaskDetailSerializer  # Serializer to use for the TaskDetail model
    )
