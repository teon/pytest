from django.db import models
from django.utils import timezone
import re

class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ["-published_date"]

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def is_valid(self):
        title_regex = re.compile("[a-zA-Z]+")
        valid = title_regex.match(self.title)
        return bool(valid)

    def __str__(self):
        return self.title
