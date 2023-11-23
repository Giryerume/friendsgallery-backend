from rest_framework import serializers
from photos.models import Photo
from approve.serializers import ApproveSerializer
from comments.serializers import CommentSerializer
from likes.serializers import LikeSerializer


class PhotoSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.username')
    comments=CommentSerializer(many=True, read_only=True)
    likes=LikeSerializer(many=True, read_only=True)
    approve=ApproveSerializer(many=True, read_only=True)
    class Meta:
        model=Photo
        fields=('id', 'user', 'title', 'comment', 'image', 'comments', 'likes', 'approve')
