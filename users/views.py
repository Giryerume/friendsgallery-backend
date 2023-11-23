import pandas as pd
from django.shortcuts import get_object_or_404, render
from . serializers import UserSerializer
from rest_framework import permissions, status, viewsets 
from rest_framework.response import Response
from django.contrib.auth.models import User


# Create your views here.
class UserViewSet(viewsets.ViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    # permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def list(self, request):
        queryset=User.objects.all()
        serializer=UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk):
        queryset=User.objects.all()
        user=get_object_or_404(queryset, pk=pk)
        serializer=UserSerializer(user)
        return Response(serializer.data)
