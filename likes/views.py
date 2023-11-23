from django.shortcuts import get_object_or_404, render
from rest_framework import permissions, serializers, viewsets
from photos.models import Photo
from likes.models import Like
from likes.serializers import LikeSerializer
from likes.permissions import HasSelfLikeOrReadyOnly


# Create your views here.
class LikeViewSet(viewsets.ModelViewSet):
    queryset=Like.objects.all()
    serializer_class=LikeSerializer
    permission_classes=[permissions.IsAuthenticated, HasSelfLikeOrReadyOnly]
    
    def perform_create(self, serializer):
        queryset=Like.objects.all()
        photo_pk=self.request.data['photo']
        photo_instance=get_object_or_404(Photo, pk=photo_pk)
        already_liked=Like.objects.filter(photo=photo_instance, user=self.request.user).exists()
        
        if already_liked:
            raise serializers.ValidationError({"message":"You've already liked this photo"})
        else:
            serializer.save(user=self.request.user, photo=photo_instance)
