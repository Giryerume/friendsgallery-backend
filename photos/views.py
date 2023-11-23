from django.shortcuts import render
from rest_framework import permissions, viewsets
from approve.models import Approve
from . models import Photo
from . serializers import PhotoSerializer
from user_profile.permissions import IsUserOrReadOnly


# Create your views here.
class PhotoViewSet(viewsets.ModelViewSet):
    queryset=Photo.objects.all()
    serializer_class=PhotoSerializer
    permission_classes=[permissions.IsAdminUser]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ApprovedPhotosViewSet(viewsets.ModelViewSet):
    approved_photos=Approve.objects.values_list('photo', flat=True)
    queryset=Photo.objects.filter(id__in=approved_photos)
    serializer_class=PhotoSerializer
    permission_classes=[permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
