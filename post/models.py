from django.db import models

from author.models import Author


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Image(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="posts")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')


class HashTag(models.Model):
    title = models.CharField(max_length=150)
    post = models.ManyToManyField(Post)

