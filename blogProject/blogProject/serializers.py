from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' # You can use '__all__' or list specific fields like ['field1', 'field2']