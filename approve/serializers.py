from rest_framework import serializers
from approve.models import Approve


class ApproveSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.username')

    class Meta:
        model=Approve
        fields=('id', 'photo', 'user')
