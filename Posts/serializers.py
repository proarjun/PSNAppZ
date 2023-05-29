from rest_framework import serializers
from .models import Posts

  
class PostsSerializer(serializers.Serializer):

    caption = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=2500)
    tags = serializers.CharField(max_length=100)
    created_date = serializers.DateField(read_only = True)
    image = serializers.ImageField()

    def create(self, validated_data):        
        posts = Posts.objects.create(**validated_data)
        return posts

   