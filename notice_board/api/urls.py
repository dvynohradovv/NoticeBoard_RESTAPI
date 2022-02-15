from django.urls import path, include
from . import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('users/', views.UserListView.as_view()),
    path('users/<int:pk>/', views.UserDetailView.as_view()),

    path('posts/', views.PostListView.as_view()),
    path('posts/<int:pk>/', views.PostDetailView.as_view()),

    path('post_likes/', views.PostLikeListView.as_view()),
    path('post_likes/<int:pk>/', views.PostLikeDetailView.as_view()),

    path('analytics/', views.analytics_likes_by_date_view),
]
