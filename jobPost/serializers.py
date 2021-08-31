from rest_framework import serializers
from jobPost.models import Post


class GetPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class MakePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'slug',
            'description'
        ]
