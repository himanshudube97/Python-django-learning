from rest_framework import serializers
from .models import Drink

#A serializer in Python, particularly in the context of Django REST Framework (DRF), 
    # is a class that transforms complex data types (like Django models or Python objects) into formats that are easy to render into JSON, XML, or other content types for APIs. 
# Serializers also handle the reverse process: deserializing data from these formats back into complex Python objects or model instances.
class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']