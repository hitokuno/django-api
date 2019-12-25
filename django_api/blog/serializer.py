# coding: utf-8

from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        extra_kwargs = { 'id': { 'read_only': False } }

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'text', 'created_date', 'published_date', 'attach')
        read_only_fields = ('created_at', 'updated_at')

    def create(self, validated_data):
        user_data = validated_data.pop('author')
        user = User.objects.get(pk=user_data['id'])
        post = Post.objects.create(author=user, **validated_data)
        return post

