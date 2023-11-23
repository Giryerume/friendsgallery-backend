from django.shortcuts import render
from rest_framework import permissions, viewsets
from comments.models import Comment
from comments.serializers import CommentSerializer
from user_profile.permissions import IsUserOrReadOnly


# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes=[permissions.IsAuthenticated, IsUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
