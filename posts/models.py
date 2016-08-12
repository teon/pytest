from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey('auth.User', related_name='posts', null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ["-published_date"]

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
