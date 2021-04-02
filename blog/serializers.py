from .models import Category, Post, Tag
from rest_framework import serializers
from django.contrib.auth.models import User

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "name",
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
        ]

class PostListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author = UserSerializer()

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'created_time',
            'excerpt',
            'category',
            'author',
            'views',
        ]


class PostRetrieveSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author = UserSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "body",
            "created_time",
            "modified_time",
            "excerpt",
            "views",
            "category",
            "author",
            "tags",
        ]
