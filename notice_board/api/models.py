from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='detail', primary_key=True, to_field="id")
    last_request = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"Detailf for {self.user.id}: {self.user.username}"


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.id}: {self.title}, by {self.owner}."


class PostLike(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    liker = models.ForeignKey(User, related_name='liked', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
        unique_together = [['liker', 'post']]

    def __str__(self):
        return f"{self.liker.username} like {self.post}"
