from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Post, PostLike, UserDetail


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner', 'likes']


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    liked = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'liked']


class UserDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    last_login = serializers.ReadOnlyField(source="user.last_login")

    class Meta:
        model = UserDetail
        fields = ["user", "last_request", "last_login"]


class PostLikeSerializer(serializers.ModelSerializer):
    liker = serializers.ReadOnlyField(source='liker.username')

    class Meta:
        model = PostLike
        fields = ['id', 'created', 'liker', 'post']
