from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        exclude_fields = self.context.get('exclude', [])
        for field in exclude_fields:
            validated_data.pop(field, None)
        return super().update(instance, validated_data)
        
    class Meta:
        model = Member
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}