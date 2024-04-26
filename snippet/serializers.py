from rest_framework import serializers
from .models import snippet_1

class snippet_1Serializer(serializers.ModelSerializer):
    class Meta:
        model = snippet_1
        fields = ['created','title', 'code']
        
    def create(self, validated_data):
        return snippet_1.objects.create(validated_data)