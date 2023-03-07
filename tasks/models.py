from django.contrib.auth.models import AbstractUser
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_complete = models.BooleanField()
    tag = models.ManyToManyField(
        Tag,
        related_name="tasks",
    )

    class Meta:
        ordering = ["is_complete", "-datetime"]

    def __str__(self):
        return self.content


