from rest_framework import serializers
from . models import Comment

class CommentSerializer(serializers.ModelSerializer):
    commented_by=serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model=Comment
        fields=('id', 'content', 'date', 'commented_by', 'photo')
