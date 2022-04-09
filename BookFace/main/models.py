from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, default=None, blank=True)
    city = models.CharField(max_length=32, null=True, default=None, blank=True)


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=64)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


class CommentBlog(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    content = models.TextField()


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.DO_NOTHING)
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.DO_NOTHING)
    msg_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
