from django.shortcuts import render
from user_profile.models import UserProfile
from user_profile.serializers import UserProfileSerializer
from rest_framework import viewsets, permissions
from . permissions import IsUserOrReadOnly

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)