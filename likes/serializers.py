from rest_framework import serializers
from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model=Like
        fields=('id', 'photo', 'user')
