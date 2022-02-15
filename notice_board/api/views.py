from django.db import IntegrityError
from django.contrib.auth.models import User
from django.db.models import Q, Count
from django.db.models.functions import TruncDay
from django.utils.dateparse import parse_date

from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import serializers
from .models import Post, PostLike, UserDetail
from .permissions import IsOwnerOrReadOnly, IsLikerOrReadOnly


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = serializers.UserDetailSerializer


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class PostLikeListView(generics.ListCreateAPIView):
    queryset = PostLike.objects.all()
    serializer_class = serializers.PostLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(liker=self.request.user)

    def create(self, request, *args, **kwargs):
        # Check for DB error from UNIQUE
        # One like for one post from one user ONLY
        try:
            return super(generics.ListCreateAPIView, self).create(request, *args, **kwargs)
        except IntegrityError:
            content = {'error': 'IntegrityError'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class PostLikeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostLike.objects.all()
    serializer_class = serializers.PostLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsLikerOrReadOnly]


@api_view()
def analytics_likes_by_date_view(request):
    try:
        params = {
            "date_from": parse_date(request.query_params.get('date_from')),
            "date_to": parse_date(request.query_params.get('date_to'))
        }
        queryset = Post.objects \
            .annotate(day=TruncDay('created')) \
            .values('day') \
            .annotate(likes_count=Count('likes'))
        return Response(queryset)
    except (ValueError, TypeError) as ex:
        content = {"error": repr(ex)}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
