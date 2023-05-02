from rest_framework import serializers
from .models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        extra_kwargs = {'senha': {'write_only': True}}

