from django.shortcuts import render, get_object_or_404
from rest_framework import permissions, serializers, viewsets
from photos.models import Photo
from approve.models import Approve
from approve.serializers import ApproveSerializer


# Create your views here.
class ApproveViewSet(viewsets.ModelViewSet):
    queryset=Approve.objects.all()
    serializer_class=ApproveSerializer
    permission_classes=[permissions.IsAdminUser]
    
    def perform_create(self, serializer):
        photo_pk=self.request.data['photo']
        photo_instance=get_object_or_404(Photo, pk=photo_pk)
        already_approved=Approve.objects.filter(photo=photo_instance).exists()
        
        if already_approved:
            raise serializers.ValidationError({"message":"This photo has already been approved"})
        else:
            serializer.save(user=self.request.user, photo=photo_instance)
