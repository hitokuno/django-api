# coding: utf-8

import django_filters
from rest_framework import viewsets, filters

from django.contrib.auth.models import User
from .models import Post
from .serializer import UserSerializer, PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_fields = ('author', 'title')

