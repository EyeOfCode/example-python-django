from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'username', 'email', 'password', 'address', 'phone', 'role', 'is_active', 'createdAt', 'updatedAt')
        extra_kwargs = {'password': {'write_only': True}}