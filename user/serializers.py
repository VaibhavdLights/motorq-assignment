from rest_framework import serializers

class UserListSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)