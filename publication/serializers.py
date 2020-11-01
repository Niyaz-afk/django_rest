from rest_framework import serializers
from .models import Post
from datetime import datetime
class PostSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    date = serializers.CharField()



    def create(self,validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.date = validated_data.get('date', instance.body)
        instance.save()
        return instance