from django.contrib.auth.models import User
from django.db import models


class Topic(models.Model):
    """Model definition for Topic."""

    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name = 'topic'
        verbose_name_plural = 'topics'

    def __str__(self):
        return self.name


class Entry(models.Model):
    """Model definition for Entry."""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        verbose_name = 'entry'
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.title
